#!/usr/bin/env python3
"""
Generic Semantic Model Runner
"""

import pandas as pd
import sys
import os
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import src as copper

def run_semantic_model(model_path, data_path):
    df = pd.read_csv(data_path)
    model = copper.load(model_path)
    
    print(f"Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Model: {model.name}")
    print(f"Description: {model.description}")
    
    print(f"\nDimensions ({len(model.dimensions)}): {list(model.dimensions.keys())}")
    print(f"Measures ({len(model.measures)}): {list(model.measures.keys())}")
    
    if model.dimensions:
        print(f"\nDimensions:")
        for dim_name, dimension in model.dimensions.items():
            print(f"{dimension.label}: {dimension.expression}")
            print()
    
    if model.measures:
        print(f"\nMeasures:")
        
        data_dict = {}
        if hasattr(model, 'datasources') and model.datasources:
            for ds_name, ds_config in model.datasources.items():
                data_dict[ds_name] = df
        elif hasattr(model, 'tables') and model.tables:
            for table_name, table_config in model.tables.items():
                data_dict[table_name] = df
        else:
            data_dict = {'default_table': df}
        
        for measure_name, measure in model.measures.items():
            print(f"{measure.label}: {measure.expression}")
            
            query = copper.Query(model).measures([measure_name])
            result = query.to_pandas(data_dict)
            value = result[measure_name].iloc[0]
            
            if hasattr(measure, 'format') and measure.format:
                print(f"  Result: {measure.format % value}")
            else:
                print(f"  Result: {value}")
            print()
    
    print(f"\nDataset Overview:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    print(f"\nSample Data (first 3 rows):")
    print(df.head(3).to_string())

def main():
    parser = argparse.ArgumentParser(description='Run semantic models with their datasets')
    parser.add_argument('model_path', help='Path to the semantic model YAML file')
    parser.add_argument('data_path', help='Path to the CSV data file')
    
    args = parser.parse_args()
    run_semantic_model(args.model_path, args.data_path)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ufc_dir = os.path.join(script_dir, '..', 'examples', 'ufc')
        model_path = os.path.join(ufc_dir, 'fight_analysis.yaml')
        data_path = os.path.join(ufc_dir, 'ufc_fights_all.csv')
        
        if os.path.exists(model_path) and os.path.exists(data_path):
            run_semantic_model(model_path, data_path)
        else:
            print("Usage: python semantic_model_runner.py <model_path> <data_path>")
            print("Example: python semantic_model_runner.py fight_analysis.yaml ufc_fights_all.csv")
    else:
        main()