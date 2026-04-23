import html
import pandas as pd
import folium
from datetime import datetime
from src.constants import (
    ENRICHED_CSV
)


def load_accommodation_data(csv_path=ENRICHED_CSV):
    """
    Load enriched accommodation data from CSV.
    
    Args:
        csv_path (str): Path to enriched CSV file
    
    Returns:
        pd.DataFrame: Dataframe with accommodation data (filtered for valid coordinates)
    """
    df = pd.read_csv(csv_path)
    # Filter rows with valid coordinates
    df_map = df.dropna(subset=['latitude', 'longitude'])
    return df_map


def create_base_map(df_map):
    """
    Create base folium map with accommodation markers.
    
    Args:
        df_map (pd.DataFrame): Dataframe with accommodation data
    
    Returns:
        folium.Map: Map object with accommodation markers
    """
    center_lat = df_map['latitude'].mean()
    center_lng = df_map['longitude'].mean()
    
    m = folium.Map(
        location=[center_lat, center_lng],
        zoom_start=4,
        tiles='OpenStreetMap'
    )
    
    # Add accommodation markers (blue)
    for idx, row in df_map.iterrows():
        popup_text = (
            f"<b>{html.escape(str(row['name']))}</b><br>"
            f"{html.escape(str(row['city']))}, {html.escape(str(row['country']))}<br>"
            f"Your Rating: {html.escape(str(row['my_rating']))}/5<br>"
            f"Google Rating: {html.escape(str(row['google_rating']))}<br>"
            f"Dates: {html.escape(str(row['dates_stayed']))}<br>"
            f"<br><i>Comment:</i><br>{html.escape(str(row['comment']))}"
        )
        
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=row['name'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)
    
    return m


