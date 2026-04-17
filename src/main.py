"""
Workflow to enrich data and or generate the interactive map
"""

import argparse
import time
import sys
from pathlib import Path
from src.enrich_data import enrich_accommodations
from src.map_builder import create_base_map, load_accommodation_data
from src.constants import ACCOMMODATIONS_CSV, ENRICHED_CSV, MAP_OUTPUT_FILE
import pandas as pd
import os

def enrich_data():
    print("=" * 60)
    print("ACCOMMODATION ANALYSIS - Data Enrichment")
    print("=" * 60)
    
    try:
        # Run enrichment
        start_time = time.time()
        df_enriched = enrich_accommodations(ACCOMMODATIONS_CSV, ENRICHED_CSV)
        elapsed = time.time() - start_time
        
        # Print summary
        print()
        print("=" * 70)
        print("✓ ENRICHMENT COMPLETE")
        print("=" * 70)
        print(f"Processed:  {len(df_enriched)} accommodations")
        print(f"Time:       {elapsed:.2f}s")
        print(f"Output:     {ENRICHED_CSV}")
        print("=" * 70)
        
        return 0
    
    except FileNotFoundError as e:
        print(f"\n✗ ERROR: {e}", file=sys.stderr)
        return 1
    
    except ValueError as e:
        print(f"\n✗ ERROR: {e}", file=sys.stderr)
        print("  Make sure GP_API_KEY environment variable is set", file=sys.stderr)
        return 1
    
    except Exception as e:
        print(f"\n✗ ERROR: {e}", file=sys.stderr)
        return 1

def build_map():
    
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
    # Ensure output directory exists then save map
    out_dir = os.path.dirname(MAP_OUTPUT_FILE) or '.'
    os.makedirs(out_dir, exist_ok=True)
    m.save(MAP_OUTPUT_FILE)
    print(f"Map saved to {MAP_OUTPUT_FILE}")
    
    # Summary
    print("\n" + "=" * 60)
    print("COMPLETE!")
    print("=" * 60)

def main():
    """
    Enrich and Generate map from accomodation data.
    """
    parser = argparse.ArgumentParser(
        description="Enrich data with google places API and or build map interactive map"
    )

    parser.add_argument(
        '--enrichdata-only',
        action='store_true',
        help="Only run the data enrichment step (no map generation)"
    )
    
    parser.add_argument(
        '--buildmap-only',
        action='store_true',
        help="Only run the map building step (no data enrichment)"
    )
    
    args = parser.parse_args()

    # fail if both args are inputted
    if args.enrichdata_only and args.buildmap_only:
        parser.error("Cannot specify both --enrichdata-only and --buildmap-only")
    
    # If neither arg is specified, run both steps
    if not args.enrichdata_only and not args.buildmap_only:
        if enrich_data() != 0:
            sys.exit(1)
        build_map()
    elif args.enrichdata_only:
        if enrich_data() != 0:
            sys.exit(1)
    elif args.buildmap_only:
        build_map()

if __name__ == "__main__":
    main()
