"""
Configuration and constants for accommodation analysis.
"""

import os

# File paths
DATA_DIR = 'data'
ACCOMMODATIONS_CSV = os.path.join(DATA_DIR, 'accommodations.csv')
ENRICHED_CSV = os.path.join(DATA_DIR, 'accommodations_enriched.csv')
OUTPUTS_DIR = 'outputs'
MAP_OUTPUT_FILE = os.path.join(OUTPUTS_DIR, 'index.html')

# API configuration
GOOGLE_PLACES_API_KEY = os.environ.get('GP_API_KEY')



