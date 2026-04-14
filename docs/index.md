---
layout: default
title: "Home"
permalink: /
---

<div class="hero-section bg-primary text-white py-5 mb-5">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <h1 class="display-4 fw-bold mb-3">Southeast Asia Accommodation Analysis</h1>
                <p class="lead mb-4">
                    An interactive exploration of accommodation reviews from a 6-month backpacking trip through Southeast Asia.
                    Discover patterns in ratings, locations, and linguistic analysis of travel experiences.
                </p>
                <div class="d-flex gap-3">
                    <a href="{{ '/map' | relative_url }}" class="btn btn-light btn-lg">
                        <i class="fas fa-map me-2"></i>View Interactive Map
                    </a>
                    <a href="{{ '/blog' | relative_url }}" class="btn btn-outline-light btn-lg">
                        <i class="fas fa-blog me-2"></i>Read Analysis
                    </a>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="stats-card bg-white text-dark p-4 rounded shadow">
                    <h3 class="h4 mb-3">Trip Statistics</h3>
                    <div class="row text-center">
                        <div class="col-6 col-md-3 mb-3">
                            <div class="stat-number display-6 fw-bold text-primary">68</div>
                            <div class="stat-label small">Accommodations</div>
                        </div>
                        <div class="col-6 col-md-3 mb-3">
                            <div class="stat-number display-6 fw-bold text-success">7</div>
                            <div class="stat-label small">Countries</div>
                        </div>
                        <div class="col-6 col-md-3 mb-3">
                            <div class="stat-number display-6 fw-bold text-info">6</div>
                            <div class="stat-label small">Months</div>
                        </div>
                        <div class="col-6 col-md-3 mb-3">
                            <div class="stat-number display-6 fw-bold text-warning">3.7</div>
                            <div class="stat-label small">Avg Rating</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="container">
    <div class="row">
        <div class="col-lg-8">
            <section class="mb-5">
                <h2 class="h3 mb-4">
                    <i class="fas fa-chart-line me-2 text-primary"></i>
                    Latest Analysis
                </h2>

                {% for post in site.posts limit:3 %}
                <article class="card mb-3 shadow-sm">
                    <div class="card-body">
                        <h3 class="card-title h5">
                            <a href="{{ post.url | relative_url }}" class="text-decoration-none">
                                {{ post.title }}
                            </a>
                        </h3>
                        <p class="card-text text-muted small mb-2">
                            <i class="fas fa-calendar me-1"></i>{{ post.date | date: "%B %d, %Y" }}
                            {% if post.author %}
                            <span class="ms-3">
                                <i class="fas fa-user me-1"></i>{{ post.author }}
                            </span>
                            {% endif %}
                        </p>
                        <p class="card-text">
                            {{ post.excerpt | strip_html | truncate: 150 }}
                        </p>
                        <a href="{{ post.url | relative_url }}" class="btn btn-primary btn-sm">
                            Read More <i class="fas fa-arrow-right ms-1"></i>
                        </a>
                    </div>
                </article>
                {% endfor %}

                <div class="text-center">
                    <a href="{{ '/blog' | relative_url }}" class="btn btn-outline-primary">
                        View All Posts <i class="fas fa-blog ms-1"></i>
                    </a>
                </div>
            </section>
        </div>

        <div class="col-lg-4">
            <section class="mb-5">
                <h3 class="h4 mb-3">
                    <i class="fas fa-map-marked-alt me-2 text-success"></i>
                    Quick Map Access
                </h3>
                <div class="card">
                    <div class="card-body">
                        <p class="mb-3">Explore my accommodation locations interactively:</p>
                        <a href="{{ '/map' | relative_url }}" class="btn btn-success w-100">
                            <i class="fas fa-map me-2"></i>Open Interactive Map
                        </a>
                        <p class="text-muted small mt-2 mb-0">
                            <i class="fas fa-info-circle me-1"></i>
                            Map shows all 68 accommodations with ratings and reviews
                        </p>
                    </div>
                </div>
            </section>

            <section class="mb-5">
                <h3 class="h4 mb-3">
                    <i class="fas fa-chart-bar me-2 text-info"></i>
                    Key Insights
                </h3>
                <div class="list-group">
                    <div class="list-group-item">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">Top Countries</h5>
                        </div>
                        <p class="mb-1">Vietnam (16), Indonesia (14), Thailand (12)</p>
                    </div>
                    <div class="list-group-item">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">Common Themes</h5>
                        </div>
                        <p class="mb-1">Location, atmosphere, cleanliness</p>
                    </div>
                    <div class="list-group-item">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">Rating Range</h5>
                        </div>
                        <p class="mb-1">2.0 to 5.0 stars (avg 3.72)</p>
                    </div>
                </div>
            </section>

            <section>
                <h3 class="h4 mb-3">
                    <i class="fab fa-github me-2 text-dark"></i>
                    Project Links
                </h3>
                <div class="d-grid gap-2">
                    <a href="https://github.com/rhiannaleslie/accomodation-analysis" class="btn btn-outline-dark" target="_blank">
                        <i class="fab fa-github me-2"></i>View Source Code
                    </a>
                    <a href="https://github.com/rhiannaleslie/accomodation-analysis/blob/main/notebooks/comment-nlp-analysis.ipynb" class="btn btn-outline-dark" target="_blank">
                        <i class="fas fa-code me-2"></i>NLP Analysis Notebook
                    </a>
                    <a href="https://github.com/rhiannaleslie/accomodation-analysis/tree/main/data" class="btn btn-outline-dark" target="_blank">
                        <i class="fas fa-database me-2"></i>Raw Data
                    </a>
                </div>
            </section>
        </div>
    </div>
</div>