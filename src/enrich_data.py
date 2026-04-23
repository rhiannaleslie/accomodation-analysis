"""
Enrich accommodation data with Google Places API information.
"""

import requests
import pandas as pd
import os
from pathlib import Path
import src.constants as constants

API_KEY = constants.GOOGLE_PLACES_API_KEY


def get_place_data(query):
    """
    Fetch place data from Google Places API.
    
    Args:
        query (str): Search query (e.g., "Accommodation Name, City, Country")
    
    Returns:
        dict: Place data with name, lat, lng, google_rating, review_count, or None if not found
    """
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if data["results"]:
        result = data["results"][0]
        return {
            "name": result["name"],
            "lat": result["geometry"]["location"]["lat"],
            "lng": result["geometry"]["location"]["lng"],
            "google_rating": result.get("rating"),
            "review_count": result.get("user_ratings_total")
        }
    return None


def enrich_accommodations(input_csv, output_csv):
    """
    Enrich accommodation data with Google Places API information.
    
    Loads raw accommodations from input_csv, fetches Google Places data for each,
    combines the data, and saves enriched results to output_csv.
    
    Args:
        input_csv (str): Path to input CSV with base accommodation data
                         Expected columns: name, city, country, my_rating, comment, dates_stayed
        output_csv (str): Path to output CSV for enriched data
                          Will include: latitude, longitude, google_rating, review_count
    
    Returns:
        pd.DataFrame: Enriched accommodation dataframe
    
    Raises:
        FileNotFoundError: If input_csv does not exist
        ValueError: If Google API key is not configured
        Exception: If any API call fails (fail-fast behavior)
    """
    # Validate preconditions
    if not os.path.exists(input_csv):
        raise FileNotFoundError(f"Input CSV not found: {input_csv}")
    
    if not API_KEY:
        raise ValueError("GOOGLE_PLACES_API_KEY environment variable not set")
    
    # Load accommodations
    df = pd.read_csv(input_csv)
    accommodations = df.to_dict('records')
    
    print(f"Loading {len(accommodations)} accommodations from {input_csv}")
    
    enriched_accommodations = []
    
    # Enrich each accommodation
    for idx, accommodation in enumerate(accommodations, 1):
        accommodation_name = accommodation['name']
        query = f"{accommodation['name']}, {accommodation['city']}, {accommodation['country']}"
        
        print(f"[{idx}/{len(accommodations)}] Enriching: {accommodation_name}...", end=" ", flush=True)
        
        try:
            place_data = get_place_data(query)
            
            if place_data:
                enriched_row = {
                    **accommodation,
                    "latitude": place_data["lat"],
                    "longitude": place_data["lng"],
                    "google_rating": place_data["google_rating"],
                    "review_count": place_data["review_count"]
                }
                print("✓")
            else:
                enriched_row = {
                    **accommodation,
                    "latitude": None,
                    "longitude": None,
                    "google_rating": None,
                    "review_count": None
                }
                print("⚠ (Not found in Google Places)")
            
            enriched_accommodations.append(enriched_row)
        
        except Exception as e:
            print(f"✗ ERROR")
            raise Exception(f"Failed to enrich '{accommodation_name}': {str(e)}") from e
    
    # Create enriched dataframe
    df_enriched = pd.DataFrame(enriched_accommodations)
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_csv) or '.'
    os.makedirs(output_dir, exist_ok=True)
    
    # Save enriched data
    df_enriched.to_csv(output_csv, index=False)
    print(f"\n✓ Enriched data saved to {output_csv}")
    print(f"  Columns: {', '.join(df_enriched.columns.tolist())}")
    
    return df_enriched