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
from bs4 import BeautifulSoup

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

def align_dataframe_columns(df, existing_col_names):
    """
    Align DataFrame columns with existing table schema
    Add missing columns with NULL values, remove extra columns
    """
    # Create a copy to avoid modifying original
    df_aligned = df.copy()
    
    # Add missing columns with NULL values
    for col in existing_col_names:
        if col not in df_aligned.columns:
            df_aligned[col] = None
            print(f"      Added missing column: {col}")
    
    # Remove extra columns not in existing schema
    extra_cols = [col for col in df_aligned.columns if col not in existing_col_names]
    if extra_cols:
        print(f"      Dropping extra columns: {extra_cols}")
        df_aligned = df_aligned.drop(columns=extra_cols)
    
    # Reorder columns to match existing table
    df_aligned = df_aligned[existing_col_names]
    
    return df_aligned

def parse_html_file(html_file, target_sheet_name):
    """
    Parse HTML file that contains demographic data tables
    Returns DataFrame for the target sheet name
    """
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'lxml')
        
        # Find all tables in the HTML
        tables = soup.find_all('table')
        
        if not tables:
            print(f"    No tables found in HTML file")
            return None
        
        # For CPS HTML files, usually the first large table contains the data
        # Try to find a table that looks like demographic data
        for i, table in enumerate(tables):
            try:
                df = pd.read_html(str(table), header=0)[0]
                
                # Check if this looks like a demographic data table
                if len(df) > 10 and len(df.columns) > 5:  # Reasonable size for demographics
                    print(f"    Found suitable table {i+1} with {df.shape[0]} rows, {df.shape[1]} columns")
                    return df
                    
            except Exception as e:
                continue
        
        # If no suitable table found, try the largest table
        if tables:
            try:
                df = pd.read_html(str(tables[0]), header=0)[0]
                print(f"    Using first table as fallback: {df.shape[0]} rows, {df.shape[1]} columns")
                return df
            except Exception as e:
                print(f"    Error parsing HTML table: {e}")
                return None
        
        return None
        
    except Exception as e:
        print(f"    Error parsing HTML file: {e}")
        return None

def parse_excel_sheet(excel_file, sheet_name):
    """
    Parse Excel sheet with multi-row headers
    Returns DataFrame with clean column names and no percentage columns
    """
    print(f"  Processing sheet: {sheet_name}")
    
    # Determine engine based on file extension and try multiple engines
    file_path = str(excel_file)
    engine = None
    
    if file_path.endswith('.xlsx'):
        engine = 'openpyxl'
    elif file_path.endswith('.xls'):
        engine = 'xlrd'
    
    # Check if file is actually HTML disguised as Excel
    try:
        with open(excel_file, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip().lower()
            if ('<!doctype html' in first_line or 
                first_line.startswith('<html') or 
                '<html' in first_line):
                print(f"    Detected HTML file disguised as Excel, parsing HTML tables")
                return parse_html_file(excel_file, sheet_name)
    except Exception:
        pass  # Continue with Excel parsing
    
    # Try multiple engines if format detection fails
    for attempt_engine in [engine, 'xlrd', 'openpyxl', None]:
        try:
            df_raw = pd.read_excel(excel_file, sheet_name=sheet_name, header=None, engine=attempt_engine)
            break
        except Exception as e:
            if attempt_engine is None:
                print(f"    Error: Could not read with any engine: {e}")
                return None
            continue
    
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

def import_demographics_file(excel_file, school_year, conn, global_tables_created):
    """Import all sheets from a demographics Excel file"""
    print(f"\nImporting {excel_file} for school year {school_year}")
    
    # Check if file is actually HTML disguised as Excel
    try:
        with open(excel_file, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip().lower()
            if ('<!doctype html' in first_line or 
                first_line.startswith('<html') or 
                '<html' in first_line):
                print(f"  Detected HTML file disguised as Excel")
                return import_html_demographics_file(excel_file, school_year, conn, global_tables_created)
    except Exception:
        pass  # Continue with Excel parsing
    
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
            
            # Create or append to table based on global state
            try:
                if table_name in global_tables_created:
                    # For append, we need to handle schema mismatches
                    # Get existing table schema first
                    existing_columns = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
                    existing_col_names = [col[1] for col in existing_columns]
                    
                    # Align new DataFrame columns with existing table
                    df_aligned = align_dataframe_columns(df, existing_col_names)
                    
                    # Append to existing table
                    df_aligned.to_sql(table_name, conn, if_exists='append', index=False)
                    print(f"    Appended to {table_name} table")
                else:
                    # Create new table (replace if exists)
                    df.to_sql(table_name, conn, if_exists='replace', index=False)
                    print(f"    Created {table_name} table")
                    global_tables_created.add(table_name)
            except Exception as e:
                print(f"    Error importing to {table_name}: {e}")
                # Try to continue with next sheet
                continue
            
            # Get final row count
            result = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
            total_rows = result[0]
            print(f"    {table_name} now has {total_rows} total rows")
            processed_tables.append(table_name)
        
        return processed_tables
        
    except Exception as e:
        print(f"Error processing {excel_file}: {e}")
        return []

def import_html_demographics_file(html_file, school_year, conn, global_tables_created):
    """Import demographics data from HTML file disguised as Excel"""
    try:
        # Parse HTML and extract main demographic table
        df = parse_html_file(html_file, 'Schools')  # Try to get schools data
        
        if df is None or df.empty:
            print(f"  No usable data found in HTML file")
            return []
        
        # Add school year as first column
        df.insert(0, 'school_year', school_year)
        
        # Clean column names
        df.columns = [clean_column_name(col) for col in df.columns]
        
        # Remove percentage columns
        pct_columns = [col for col in df.columns if 'pct' in col.lower() or 'percent' in col.lower()]
        if pct_columns:
            df = df.drop(columns=pct_columns)
            print(f"  Removed {len(pct_columns)} percentage columns from HTML data")
        
        # Determine table type based on content (default to schools for HTML files)
        table_name = 'schools'
        
        # Import to database
        try:
            if table_name in global_tables_created:
                # Get existing table schema and align columns
                existing_columns = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
                existing_col_names = [col[1] for col in existing_columns]
                df_aligned = align_dataframe_columns(df, existing_col_names)
                df_aligned.to_sql(table_name, conn, if_exists='append', index=False)
                print(f"  Appended HTML data to {table_name} table")
            else:
                df.to_sql(table_name, conn, if_exists='replace', index=False)
                print(f"  Created {table_name} table from HTML data")
                global_tables_created.add(table_name)
            
            # Get final row count
            result = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
            total_rows = result[0]
            print(f"  {table_name} now has {total_rows} total rows")
            
            return [table_name]
            
        except Exception as e:
            print(f"  Error importing HTML data to {table_name}: {e}")
            return []
            
    except Exception as e:
        print(f"Error processing HTML file {html_file}: {e}")
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
    global_tables_created = set()  # Track which tables have been created globally
    
    # Process each file in chronological order
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
        
        processed = import_demographics_file(file_path, school_year, conn, global_tables_created)
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