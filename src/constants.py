"""
Configuration and constants for accommodation analysis.
"""

import os

# File paths
DATA_DIR = 'data'
ACCOMMODATIONS_CSV = os.path.join(DATA_DIR, 'accommodations.csv')
ENRICHED_CSV = os.path.join(DATA_DIR, 'accommodations_enriched.csv')
MAP_OUTPUT_FILE = os.path.join(DATA_DIR, 'accommodations_map.html')

# API configuration
GOOGLE_PLACES_API_KEY = os.environ.get('GP_API_KEY')



