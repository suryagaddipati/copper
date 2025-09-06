#!/usr/bin/env python3
"""
CPS Demographics Data Import Script

This script imports Chicago Public Schools demographic Excel files into DuckDB,
handling multi-row headers, cleaning column names, and removing percentage columns.

Dependencies (added to main pyproject.toml):
- duckdb>=1.3.0
- openpyxl>=3.1.0  (for .xlsx files)  
- xlrd>=2.0.1      (for .xls files)
- pandas>=1.3.0

Run with UV (when available): uv run python examples/cps/data/import_cps_data.py
Or directly: python examples/cps/data/import_cps_data.py

Key features:
- Handles multi-row Excel headers
- Removes all percentage columns (calculable from raw data)
- Adds school_year column
- Creates clean table names without year suffixes
- Supports multiple file years for future expansion
"""

import pandas as pd
import duckdb
import os
import re
from pathlib import Path

def clean_column_name(name):
    """Clean and standardize column names"""
    if pd.isna(name) or name == '':
        return ''
    
    # Convert to string and basic cleanup
    name = str(name).strip()
    name = re.sub(r'\s+', '_', name)  # Replace spaces with underscores
    name = name.replace('/', '_').replace('\\', '_')
    name = name.replace('\n', '_').replace('\r', '')
    name = name.replace('(', '').replace(')', '')
    name = re.sub(r'_+', '_', name)  # Replace multiple underscores with single
    name = name.strip('_')
    
    return name

def parse_excel_sheet(excel_file, sheet_name):
    """
    Parse Excel sheet with multi-row headers
    Returns DataFrame with clean column names and no percentage columns
    """
    print(f"  Processing sheet: {sheet_name}")
    
    # Read raw data without headers
    df_raw = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
    
    if df_raw.empty:
        print(f"    Warning: Sheet {sheet_name} is empty")
        return None
    
    # Find data start row by looking for key patterns
    data_start_row = 0
    for i in range(min(10, len(df_raw))):
        first_cell = str(df_raw.iloc[i, 0]).strip() if not pd.isna(df_raw.iloc[i, 0]) else ''
        if first_cell in ['School ID', 'Grade Level', 'Network']:
            data_start_row = i
            break
    
    # Handle multi-row headers
    if data_start_row > 0:
        # Row above data_start_row contains main categories
        header_row1 = df_raw.iloc[data_start_row-1].fillna('')
        header_row2 = df_raw.iloc[data_start_row].fillna('')
        
        # Combine headers intelligently
        combined_headers = []
        for i, (h1, h2) in enumerate(zip(header_row1, header_row2)):
            h1_clean = clean_column_name(h1)
            h2_clean = clean_column_name(h2)
            
            # Skip percentage columns entirely
            if h2_clean in ['Pct'] or h1_clean.endswith('_Pct') or h2_clean.endswith('_Pct'):
                combined_headers.append(f'SKIP_PCT_{i}')
                continue
                
            # Combine demographic category with No/Total
            if h2_clean in ['No', 'Total'] and h1_clean:
                combined_header = f"{h1_clean}_{h2_clean}"
            elif h2_clean and h2_clean not in ['No', 'Total']:
                combined_header = h2_clean
            elif h1_clean:
                combined_header = h1_clean
            else:
                combined_header = f'column_{i}'
                
            combined_headers.append(combined_header)
        
        # Get actual data (skip header rows)
        df_data = df_raw.iloc[data_start_row+1:].reset_index(drop=True)
        df_data.columns = combined_headers
        
    else:
        # Single header row
        df_data = pd.read_excel(excel_file, sheet_name=sheet_name, header=0)
        # Clean existing column names and mark percentage columns for removal
        new_columns = []
        for col in df_data.columns:
            clean_col = clean_column_name(col)
            if 'pct' in clean_col.lower() or 'percent' in clean_col.lower():
                new_columns.append(f'SKIP_PCT_{len(new_columns)}')
            else:
                new_columns.append(clean_col)
        df_data.columns = new_columns
    
    # Remove percentage columns (marked with SKIP_PCT prefix)
    pct_columns = [col for col in df_data.columns if col.startswith('SKIP_PCT_')]
    if pct_columns:
        df_data = df_data.drop(columns=pct_columns)
        print(f"    Removed {len(pct_columns)} percentage columns")
    
    # Remove completely empty rows and columns
    df_data = df_data.dropna(how='all')  # Remove empty rows
    df_data = df_data.loc[:, ~df_data.columns.str.contains('Unnamed')]  # Remove unnamed columns
    
    print(f"    Final shape: {df_data.shape[0]} rows, {df_data.shape[1]} columns")
    
    return df_data

def import_demographics_file(excel_file, school_year, conn):
    """Import all sheets from a demographics Excel file"""
    print(f"\nImporting {excel_file} for school year {school_year}")
    
    try:
        excel_obj = pd.ExcelFile(excel_file)
        sheets_to_process = {
            'Schools': 'schools',
            'District ': 'district',  # Note the space
            'District': 'district',   # Alternative name
            'Networks': 'networks',
            'Comparison': 'comparison'
        }
        
        processed_tables = []
        
        for sheet_name in excel_obj.sheet_names:
            # Find matching table name
            table_name = None
            for pattern, target_table in sheets_to_process.items():
                if pattern.strip().lower() == sheet_name.strip().lower():
                    table_name = target_table
                    break
            
            if not table_name:
                print(f"  Skipping sheet: {sheet_name}")
                continue
                
            # Parse the sheet
            df = parse_excel_sheet(excel_file, sheet_name)
            if df is None or df.empty:
                continue
            
            # Add school year as first column
            df.insert(0, 'school_year', school_year)
            
            # Create or append to table
            if table_name in processed_tables:
                # Append to existing table
                df.to_sql(table_name, conn, if_exists='append', index=False)
                print(f"    Appended to {table_name} table")
            else:
                # Create new table (replace if exists)
                df.to_sql(table_name, conn, if_exists='replace', index=False)
                print(f"    Created {table_name} table")
                processed_tables.append(table_name)
            
            # Get final row count
            result = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
            total_rows = result[0]
            print(f"    {table_name} now has {total_rows} total rows")
        
        return processed_tables
        
    except Exception as e:
        print(f"Error processing {excel_file}: {e}")
        return []

def main():
    """Main import function"""
    print("=== CPS Demographics Data Import ===\n")
    
    # Setup paths
    data_dir = Path("downloads")
    db_file = "cps_demographics.duckdb"
    
    # Remove ALL existing CPS database files for clean start
    old_db_files = [
        "cps_demographics.duckdb",
        "cps_demographics_clean.duckdb", 
        "cps_demographics_final.duckdb"
    ]
    
    removed_count = 0
    for old_db in old_db_files:
        if os.path.exists(old_db):
            os.remove(old_db)
            print(f"Removed existing database: {old_db}")
            removed_count += 1
    
    if removed_count == 0:
        print("No existing databases to remove")
    
    # Connect to DuckDB
    conn = duckdb.connect(db_file)
    
    # Find demographics files in downloads folder
    racial_ethnic_files = list(data_dir.glob("cps_demographics_racial_ethnic_*.xlsx"))
    racial_ethnic_files.extend(list(data_dir.glob("cps_demographics_racial_ethnic_*.xls")))
    
    # Also look for EL/IEP/Economic files for future expansion
    el_iep_files = list(data_dir.glob("CPS_Demographics_LEP_IEP_EconDisadv_*.xlsx"))
    el_iep_files.extend(list(data_dir.glob("CPS_Demographics_LEP_IEP_EconDisadv_*.xls")))
    
    print(f"Found {len(racial_ethnic_files)} racial/ethnic files")
    print(f"Found {len(el_iep_files)} EL/IEP/Economic files (not processed yet)")
    
    if not racial_ethnic_files:
        print("No CPS racial/ethnic demographics files found!")
        return
    
    
    all_processed_tables = set()
    
    # Process each file
    for file_path in sorted(racial_ethnic_files):
        # Extract year from filename
        filename = file_path.name
        year_match = re.search(r'(\d{4})[_-]?(\d{4})', filename)
        if year_match:
            school_year = f"{year_match.group(1)}-{year_match.group(2)}"
        else:
            # Fallback year extraction
            year_match = re.search(r'(\d{4})', filename)
            if year_match:
                year = int(year_match.group(1))
                school_year = f"{year}-{year+1}"
            else:
                school_year = "unknown"
        
        processed = import_demographics_file(file_path, school_year, conn)
        all_processed_tables.update(processed)
    
    # Final database summary
    print(f"\n=== IMPORT COMPLETE ===")
    print(f"Database: {db_file}")
    print(f"Tables created: {len(all_processed_tables)}")
    
    for table_name in sorted(all_processed_tables):
        try:
            result = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
            row_count = result[0]
            
            # Get unique years
            years_result = conn.execute(f"SELECT DISTINCT school_year FROM {table_name} ORDER BY school_year").fetchall()
            years = [row[0] for row in years_result]
            
            print(f"  {table_name}: {row_count} rows, years: {years}")
            
            # Show sample columns (first 10)
            columns = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
            col_names = [col[1] for col in columns[:10]]
            print(f"    Sample columns: {col_names}")
            
        except Exception as e:
            print(f"  {table_name}: Error - {e}")
    
    conn.close()
    print(f"\nImport complete! Use: duckdb {db_file}")

if __name__ == "__main__":
    main()