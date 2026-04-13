# Accommodation Analysis

Visualise accomodation and ratings on an interactive map.

**File structure**

```text
.
├── data
│   ├── accommodations.csv
│   └── accommodations_enriched.csv
├── outputs
│   └── index.html
├── notebooks
│   └── get_data.ipynb
├── src
│   ├── __init__.py
│   ├── constants.py
│   ├── main.py
│   └── map_builder.py
├── pyproject.toml
└── README.md
```

**Quick setup**
1. Install dependencies and create a virtual environment using uv:

```cmd
uv sync
```

2. Activate the virtual environment:

```cmd
source .venv/bin/activate
```

3. (Optional) Set Google Places API key if you will re-enrich data:

```powershell
$env:GP_API_KEY = "your_api_key_here"
```

**Run**
- Add or edit `data/accommodations.csv`, or use `notebooks/get_data.ipynb` to interactively add entries.
- To enrich and generate the map, run the following:

```cmd
python -m src.main
```
- The generated map is served at your GitHub Pages URL root (e.g., `https://<username>.github.io/accomodation-analysis/`) after deployment.

