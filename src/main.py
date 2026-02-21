"""
Main entry point for accommodation analysis workflow.
Generates map from existing enriched data.
"""

from src.map_builder import create_base_map, load_accommodation_data
from src.constants import ENRICHED_CSV, MAP_OUTPUT_FILE
import pandas as pd
import os


def main():
    """
    Generate map from existing enriched data.
    """
    print("=" * 60)
    print("ACCOMMODATION ANALYSIS - Map Generation")
    print("=" * 60)
    
    # Check if enriched data exists
    if not os.path.exists(ENRICHED_CSV):
        raise FileNotFoundError("Enriched CSV file does not exist")
    
    # Build map
    df_map = load_accommodation_data(ENRICHED_CSV)
    
    # Create base map
    m = create_base_map(df_map)
            
    # Save map
    m.save(MAP_OUTPUT_FILE)
    print(f"Map saved to {MAP_OUTPUT_FILE}")
    
    # Summary
    print("\n" + "=" * 60)
    print("COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
