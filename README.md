# Accommodation Analysis

Visualise accomodation and ratings on an interactive map.

**File structure**

```text
.
├── data
│   ├── accommodations.csv
│   └── accommodations_enriched.csv
├── outputs
│   └── accommodations_map.html
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
1. Create a Conda environment (recommended):

```cmd
conda create --name env_name python=3.12
```

2. Activate the environment:

```cmd
conda activate env_name
```

3. Install dependencies:

```cmd
pip install -e .
```

4. (Optional) Set Google Places API key if you will re-enrich data:

```powershell
$env:GP_API_KEY = "your_api_key_here"
```

**Run**
- Add or edit `data/accommodations.csv`, or use `notebooks/get_data.ipynb` to interactively add entries.
- To enrich and generate the map, run the following in your conda env:

```cmd
python -m src.main
```
- The generated map is `outputs/accommodations_map.html`.

