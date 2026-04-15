#!/usr/bin/env python3
"""
CLI wrapper for enriching accommodation data with Google Places API information.

Usage:
    python scripts/enrich_accommodations.py                    # Use default paths from constants
    python scripts/enrich_accommodations.py --input data/accommodations.csv --output data/enriched.csv

This script loads raw accommodation data, fetches Google Places information for each
accommodation, and saves the enriched dataset with coordinates and ratings.
"""

import argparse
import sys
import time
from pathlib import Path

# Add parent directory to path so we can import src module
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.enrich_data import enrich_accommodations
from src.constants import ACCOMMODATIONS_CSV, ENRICHED_CSV


def main():
    """Parse arguments and run enrichment workflow."""
    parser = argparse.ArgumentParser(
        description="Enrich accommodation data with Google Places API information",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/enrich_accommodations.py
      Uses default paths from src/constants.py
  
  python scripts/enrich_accommodations.py --input data/accommodations.csv --output data/enriched.csv
      Use custom input/output paths
        """
    )
    
    parser.add_argument(
        '--input',
        type=str,
        default=ACCOMMODATIONS_CSV,
        help=f"Path to input CSV (default: {ACCOMMODATIONS_CSV})"
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default=ENRICHED_CSV,
        help=f"Path to output CSV (default: {ENRICHED_CSV})"
    )
    
    args = parser.parse_args()
    
    # Print header
    print("=" * 70)
    print("ACCOMMODATION DATA ENRICHMENT")
    print("=" * 70)
    print(f"Input:  {args.input}")
    print(f"Output: {args.output}")
    print("=" * 70)
    print()
    
    try:
        # Run enrichment
        start_time = time.time()
        df_enriched = enrich_accommodations(args.input, args.output)
        elapsed = time.time() - start_time
        
        # Print summary
        print()
        print("=" * 70)
        print("✓ ENRICHMENT COMPLETE")
        print("=" * 70)
        print(f"Processed:  {len(df_enriched)} accommodations")
        print(f"Time:       {elapsed:.2f}s")
        print(f"Output:     {args.output}")
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


if __name__ == "__main__":
    sys.exit(main())
