---
layout: default
title: "About"
permalink: /about
---

<div class="row">
    <div class="col-lg-8 mx-auto">
        <header class="text-center mb-5">
            <h1 class="display-5 mb-3">About This Project</h1>
            <p class="lead text-muted">
                A data-driven exploration of accommodation experiences during a Southeast Asia backpacking trip
            </p>
        </header>

        <div class="card mb-5">
            <div class="card-body">
                <h2 class="h4 mb-3">
                    <i class="fas fa-route text-primary me-2"></i>
                    The Journey
                </h2>
                <p>
                    This project analyzes my 6-month backpacking trip through Southeast Asia from March to September 2025.
                    I stayed at 68 different accommodations across 7 countries, collecting data on locations, ratings,
                    and personal reviews along the way.
                </p>

                <div class="row mt-4">
                    <div class="col-md-4 text-center">
                        <div class="stat-number display-4 fw-bold text-primary">68</div>
                        <div class="text-muted">Accommodations</div>
                    </div>
                    <div class="col-md-4 text-center">
                        <div class="stat-number display-4 fw-bold text-success">7</div>
                        <div class="text-muted">Countries</div>
                    </div>
                    <div class="col-md-4 text-center">
                        <div class="stat-number display-4 fw-bold text-info">183</div>
                        <div class="text-muted">Days</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row mb-5">
            <div class="col-md-6">
                <div class="card h-100">
                    <div class="card-header">
                        <h3 class="h5 mb-0">
                            <i class="fas fa-chart-line text-success me-2"></i>
                            Data Analysis
                        </h3>
                    </div>
                    <div class="card-body">
                        <ul class="list-unstyled">
                            <li class="mb-2">
                                <i class="fas fa-check text-success me-2"></i>
                                Accommodation ratings and reviews
                            </li>
                            <li class="mb-2">
                                <i class="fas fa-check text-success me-2"></i>
                                Geographic location analysis
                            </li>
                            <li class="mb-2">
                                <i class="fas fa-check text-success me-2"></i>
                                Temporal trend analysis
                            </li>
                            <li class="mb-2">
                                <i class="fas fa-check text-success me-2"></i>
                                NLP text analysis
                            </li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="col-md-6">
                <div class="card h-100">
                    <div class="card-header">
                        <h3 class="h5 mb-0">
                            <i class="fas fa-code text-primary me-2"></i>
                            Technical Stack
                        </h3>
                    </div>
                    <div class="card-body">
                        <ul class="list-unstyled">
                            <li class="mb-2">
                                <i class="fab fa-python text-primary me-2"></i>
                                Python (pandas, scikit-learn)
                            </li>
                            <li class="mb-2">
                                <i class="fas fa-map text-success me-2"></i>
                                Folium for interactive maps
                            </li>
                            <li class="mb-2">
                                <i class="fas fa-blog text-info me-2"></i>
                                Jekyll for this website
                            </li>
                            <li class="mb-2">
                                <i class="fab fa-github text-dark me-2"></i>
                                GitHub Pages hosting
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <div class="card">
            <div class="card-body">
                <h2 class="h4 mb-3">
                    <i class="fas fa-question-circle text-info me-2"></i>
                    Methodology
                </h2>
                <div class="row">
                    <div class="col-md-6">
                        <h4 class="h6 text-primary">Data Collection</h4>
                        <p class="small">
                            Accommodation details were collected during travel using Google Places API and personal notes.
                            Each location includes coordinates, ratings, and review text.
                        </p>

                        <h4 class="h6 text-primary">Analysis Process</h4>
                        <p class="small">
                            Data was cleaned and processed using Python. NLP techniques were applied to extract insights
                            from review text, while statistical analysis revealed patterns in ratings and locations.
                        </p>
                    </div>
                    <div class="col-md-6">
                        <h4 class="h6 text-success">Visualization</h4>
                        <p class="small">
                            Interactive maps were created with Folium, showing all accommodation locations with
                            color-coded ratings and detailed popups.
                        </p>

                        <h4 class="h6 text-success">Publication</h4>
                        <p class="small">
                            Results are published on GitHub Pages using Jekyll, making the analysis accessible
                            and interactive for anyone interested in travel data.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="text-center mt-5">
            <h2 class="h4 mb-3">Explore the Analysis</h2>
            <div class="d-flex justify-content-center gap-3">
                <a href="{{ '/map' | relative_url }}" class="btn btn-primary">
                    <i class="fas fa-map me-2"></i>Interactive Map
                </a>
                <a href="{{ '/blog' | relative_url }}" class="btn btn-success">
                    <i class="fas fa-blog me-2"></i>Analysis Blog
                </a>
                <a href="https://github.com/rhiannaleslie/accomodation-analysis" class="btn btn-dark" target="_blank">
                    <i class="fab fa-github me-2"></i>Source Code
                </a>
            </div>
        </div>
    </div>
</div>