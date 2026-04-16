# Accommodation Analysis

Visualise the accommodation and ratings and reviews from my backpacking trip on an interactive map; `https://rhiannaleslie.github.io/accomodation-analysis/`


## File Structure

```text
.
├── data
│   ├── raw
│       └── accommodations.csv
│   ├── processed
├── notebooks
│   ├── get_data.ipynb           # Data collection notebook
├── outputs
│   └── index.html               # Generated interactive map
├── src
│   ├── __init__.py
│   ├── constants.py
│   ├── enrich_data.py
│   ├── main.py
│   └── map_builder.py
├── .gitignore
├── pyproject.toml
├── README.md
└── uv.lock
```

## Setup

1. Install dependencies and create a virtual environment using uv:

```bash
uv sync
```

2. Activate the virtual environment:

```bash
source .venv/bin/activate
```

3. (Optional) Set Google Places API key if you will re-enrich data:

```bash
export GP_API_KEY="your_api_key_here"
```

## Usage

### Data

- **Data Collection**: Use `notebooks/get_data.ipynb` to interactively add accommodation entries


### Generate Interactive Map

To enrich data with google places information and generate the interactive map:

```bash
python -m src.main
```

Optional agruments to add if you only want enrich the data with the google places API or build the map:
```bash
--enrichdata-only
--buildmap-only
```


The generated map will be saved to `outputs/index.html`.



