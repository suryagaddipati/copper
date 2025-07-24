import pandas as pd
import sys
import os
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.model import load_model

def run_semantic_model(model_path):
    model = load_model(model_path)
    from pathlib import Path
    model_dir = Path(model_path).parent
    datasource = next(iter(model.datasources.values()))
    df = datasource.load(base_path=model_dir)

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
        for ds_name in model.datasources.keys():
            data_dict[ds_name] = df

        for measure_name, measure in model.measures.items():
            print(f"{measure.label}: {measure.expression}")

            try:
                value = measure.calculate(model, data_dict)

                if hasattr(measure, 'format') and measure.format:
                    print(f"  Result: {measure.format % value}")
                else:
                    print(f"  Result: {value}")
            except Exception as e:
                print(f"  Error calculating: {e}")
            print()

    print(f"\nDataset Overview:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

def main():
    parser = argparse.ArgumentParser(description='Run semantic models with their datasets')
    parser.add_argument('model_path', help='Path to the semantic model YAML file')

    args = parser.parse_args()
    run_semantic_model(args.model_path)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ufc_dir = os.path.join(script_dir, '..', 'examples', 'ufc')
        model_path = os.path.join(ufc_dir, 'fight_analysis.yaml')

        if os.path.exists(model_path):
            run_semantic_model(model_path)
        else:
            print("Usage: python semantic_model_runner.py <model_path>")
            print("Example: python semantic_model_runner.py fight_analysis.yaml")
    else:
        main()
