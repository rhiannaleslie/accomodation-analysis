# Accommodation Analysis - GitHub Pages

This repository contains the GitHub Pages website for the Southeast Asia Accommodation Analysis project. The site showcases interactive maps, data analysis, and blog posts about travel accommodation patterns.

## 🌐 Live Website

Visit the live site at: [https://rhiannaleslie.github.io/accomodation-analysis/](https://rhiannaleslie.github.io/accomodation-analysis/)

## 📁 Project Structure

```
docs/
├── _config.yml          # Jekyll configuration
├── _layouts/           # Page templates
│   ├── default.html    # Main layout
│   └── post.html       # Blog post layout
├── _pages/             # Static pages
│   ├── about.md        # About page
│   ├── blog.md         # Blog index
│   └── map.md          # Interactive map page
├── _posts/             # Blog posts
│   └── 2026-04-14-nlp-analysis-accommodation-reviews.md
├── assets/             # Static assets
│   ├── css/
│   │   └── main.css    # Custom styles
│   ├── js/
│   │   └── main.js     # Custom JavaScript
│   └── map/
│       └── index.html  # Embedded interactive map
└── index.md            # Homepage
```

## 🚀 Quick Start

### Prerequisites

1. **Ruby and Jekyll**: Install Jekyll to build the site locally
   ```bash
   gem install jekyll bundler
   ```

2. **GitHub Repository**: Set up a GitHub repository and enable GitHub Pages
   - Go to repository Settings → Pages
   - Set source to "Deploy from a branch"
   - Select "gh-pages" branch

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Install dependencies**
   ```bash
   cd docs
   bundle install
   ```

3. **Run locally**
   ```bash
   jekyll serve
   ```
   Visit `http://localhost:4000` to preview the site

### Deployment

The site is automatically deployed to GitHub Pages using the provided deployment script:

```bash
./deploy.sh
```

This script:
- Builds the Jekyll site
- Commits changes
- Pushes to the `gh-pages` branch

## 📝 Writing Blog Posts

Create new blog posts in the `docs/_posts/` directory with the format:
`YYYY-MM-DD-title.md`

Example front matter:
```yaml
---
layout: post
title: "Your Post Title"
date: 2026-04-14
author: "Your Name"
categories: [travel, analysis]
tags: [accommodation, data]
description: "Brief description of your post"
---
```

## 🗺️ Interactive Map

The interactive map is embedded from the original Folium-generated `outputs/index.html`. To update the map:

1. Run your map generation script
2. Copy the new `index.html` to `docs/assets/map/`
3. Commit and deploy

## 🎨 Customization

### Styling

- **CSS**: Edit `docs/assets/css/main.css`
- **Bootstrap**: The site uses Bootstrap 5.1.3
- **Colors**: Customize CSS variables in `main.css`

### Layout

- **Default layout**: `docs/_layouts/default.html`
- **Post layout**: `docs/_layouts/post.html`
- **Navigation**: Edit the navbar in `default.html`

### Configuration

Edit `docs/_config.yml` to change:
- Site title and description
- URL and base path
- Author information
- Plugin settings

## 📊 Data Analysis

The website showcases analysis from the Jupyter notebooks:

- **NLP Analysis**: `notebooks/comment-nlp-analysis.ipynb`
- **Sentiment Analysis**: `notebooks/sentiment-eda.ipynb`
- **Data Processing**: `src/` directory

## 🔧 Troubleshooting

### Common Issues

1. **Site not loading**: Check GitHub Pages settings and build status
2. **Map not displaying**: Ensure `docs/assets/map/index.html` exists
3. **Styles not applying**: Check CSS file paths and syntax
4. **Posts not showing**: Verify front matter and file naming

### Build Errors

Check the Jekyll build output:
```bash
cd docs
jekyll build --verbose
```

## 📄 License

This project is open source. See the main repository for licensing information.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `jekyll serve`
5. Submit a pull request

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Check the documentation in the main repository
- Review the Jekyll documentation: https://jekyllrb.com/docs/

---

*Built with Jekyll, Bootstrap, and Folium. Data analysis powered by Python and pandas.*