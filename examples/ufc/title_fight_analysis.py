#!/usr/bin/env python3
"""
UFC Title Fight Analysis
Load the fight_analysis.yaml semantic model and demonstrate Copper library functionality
"""

import pandas as pd
import sys
import os

# Add the src directory to path to import copper modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import src as copper

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load data and semantic model
    df = pd.read_csv(os.path.join(script_dir, 'ufc_fights_all.csv'))
    model = copper.load(os.path.join(script_dir, 'fight_analysis.yaml'))
    
    print(f"Dataset: {df.shape[0]} fights")
    print(f"Model: {model.name}")
    print(f"Description: {model.description}")
    
    # Show semantic model structure
    print(f"\nDimensions: {list(model.dimensions.keys())}")
    print(f"Measures: {list(model.measures.keys())}")
    
    # Manual analysis using the semantic model definitions
    print(f"\nFight Analysis:")
    
    # Total fights
    total_fights = len(df)
    print(f"Total Fights: {total_fights}")
    
    # Title fights (if column exists)
    if 'title_fight' in df.columns:
        title_fights = df[df['title_fight'] == True].shape[0]
        print(f"Title Fights: {title_fights}")
        print(f"Title Fight Rate: {title_fights/total_fights*100:.1f}%")
    
    # Fights by weight class
    if 'weight_class' in df.columns:
        weight_class_counts = df['weight_class'].value_counts().head()
        print(f"\nTop weight classes by fight count:")
        for weight_class, count in weight_class_counts.items():
            print(f"  {weight_class}: {count}")
    
    # Fight methods
    if 'method' in df.columns:
        method_counts = df['method'].value_counts().head()
        print(f"\nTop finish methods:")
        for method, count in method_counts.items():
            print(f"  {method}: {count}")
    
    # Demonstrate semantic model access
    print(f"\nSemantic Model Definitions:")
    if 'weight_class' in model.dimensions:
        dim = model.dimensions['weight_class']
        print(f"Weight Class Dimension: {dim.expression}")
    
    if 'total_fights' in model.measures:
        measure = model.measures['total_fights']
        print(f"Total Fights Measure: {measure.expression}")

if __name__ == "__main__":
    main()