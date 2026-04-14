---
layout: default
title: "Interactive Map"
permalink: /map
---

<div class="row">
    <div class="col-12">
        <div class="card">
            <div class="card-header bg-primary text-white">
                <h2 class="h4 mb-0">
                    <i class="fas fa-map-marked-alt me-2"></i>
                    Southeast Asia Accommodation Map
                </h2>
            </div>
            <div class="card-body p-0">
                <div class="map-container">
                    <!-- Embedded map from outputs/index.html -->
                    <iframe
                        src="{{ '/assets/map/index.html' | relative_url }}"
                        width="100%"
                        height="600"
                        frameborder="0"
                        allowfullscreen
                        loading="lazy">
                    </iframe>
                </div>
            </div>
            <div class="card-footer">
                <div class="row text-center">
                    <div class="col-md-3">
                        <div class="stat-number h4 text-primary mb-1">68</div>
                        <div class="small text-muted">Total Locations</div>
                    </div>
                    <div class="col-md-3">
                        <div class="stat-number h4 text-success mb-1">7</div>
                        <div class="small text-muted">Countries</div>
                    </div>
                    <div class="col-md-3">
                        <div class="stat-number h4 text-info mb-1">3.7</div>
                        <div class="small text-muted">Avg Rating</div>
                    </div>
                    <div class="col-md-3">
                        <div class="stat-number h4 text-warning mb-1">6</div>
                        <div class="small text-muted">Months</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-lg-8 mx-auto">
        <div class="card">
            <div class="card-body">
                <h3 class="h5 mb-3">Map Features</h3>
                <div class="row">
                    <div class="col-md-6">
                        <h4 class="h6 text-primary">
                            <i class="fas fa-map-marker-alt me-2"></i>Location Markers
                        </h4>
                        <p class="small mb-3">Each accommodation is marked with its exact location, rating, and key details.</p>

                        <h4 class="h6 text-success">
                            <i class="fas fa-star me-2"></i>Rating Visualization
                        </h4>
                        <p class="small mb-3">Color-coded markers show rating levels from red (low) to green (high).</p>
                    </div>
                    <div class="col-md-6">
                        <h4 class="h6 text-info">
                            <i class="fas fa-info-circle me-2"></i>Interactive Popups
                        </h4>
                        <p class="small mb-3">Click markers to see accommodation details, reviews, and Google ratings.</p>

                        <h4 class="h6 text-warning">
                            <i class="fas fa-route me-2"></i>Journey Timeline
                        </h4>
                        <p class="small mb-0">Follow my travel route chronologically through Southeast Asia.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-12 text-center">
        <p class="text-muted">
            <i class="fas fa-code me-1"></i>
            Map built with Folium and OpenStreetMap data
        </p>
    </div>
</div>