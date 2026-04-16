# Accommodation Analysis

Visualise accommodation and ratings on an interactive map, with comprehensive NLP analysis of guest comments and a web deployment option.

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

## Features

- **Interactive Map**: Visualize accommodations with ratings, prices, and locations
- **Sentiment Analysis**: Analyze guest reviews and ratings
- **NLP Trend Analysis**: Extract topics and trends from accommodation comments
- **Web Deployment**: Publish analysis results on GitHub Pages with blog functionality

## Quick Setup

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

### Data Analysis

- **Data Collection**: Use `notebooks/get_data.ipynb` to interactively add accommodation entries
- **Sentiment Analysis**: Run `notebooks/sentiment-eda.ipynb` for comprehensive sentiment analysis and EDA
- **NLP Analysis**: Execute `notebooks/comment-nlp-analysis.ipynb` for topic modeling and trend analysis of comments

### Generate Interactive Map

To enrich data and generate the interactive map:

```bash
python -m src.main
```

The generated map will be saved to `outputs/index.html`.

### Web Deployment

The project includes a complete GitHub Pages setup in the `docs/` directory:

1. **Configure Site Settings**: Edit `docs/_config.yml` with your repository details
2. **Deploy to GitHub Pages**: Run the deployment script:

```bash
cd docs
./deploy.sh
```

3. **Create Blog Posts**: Use the helper script to create new posts:

```bash
./new_post.sh "Your Post Title"
```

4. **Local Development**: Test the site locally:

```bash
cd docs
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000` to preview your site.

## Analysis Notebooks

- **`sentiment-eda.ipynb`**: Comprehensive sentiment analysis including rating distributions, text preprocessing, and sentiment classification
- **`comment-nlp-analysis.ipynb`**: Pure NLP analysis focusing on topic modeling, word frequencies, and trend identification from guest comments

## Web Features

- **Responsive Design**: Bootstrap-based layout that works on all devices
- **Embedded Map**: Interactive Folium map integrated into the web pages
- **Blog System**: Jekyll-powered blog for sharing analysis insights
- **Automated Deployment**: Scripts for easy GitHub Pages publishing
- The generated map is served at your GitHub Pages URL root (e.g., `https://<username>.github.io/accomodation-analysis/`) after deployment.

