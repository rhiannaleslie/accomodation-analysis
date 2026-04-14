---
layout: default
title: "Analysis Blog"
permalink: /blog
---

<div class="row">
    <div class="col-lg-8 mx-auto">
        <header class="text-center mb-5">
            <h1 class="display-5">
                <i class="fas fa-blog text-primary me-3"></i>
                Analysis Blog
            </h1>
            <p class="lead text-muted">
                Deep dives into accommodation data, travel patterns, and insights from Southeast Asia
            </p>
        </header>

        <!-- Blog Posts -->
        {% for post in site.posts %}
        <article class="card mb-4 shadow-sm">
            <div class="card-body">
                <div class="row">
                    <div class="col-md-12">
                        <h2 class="card-title h4 mb-2">
                            <a href="{{ post.url | relative_url }}" class="text-decoration-none text-dark">
                                {{ post.title }}
                            </a>
                        </h2>

                        <div class="post-meta text-muted small mb-3">
                            <i class="fas fa-calendar me-1"></i>
                            {{ post.date | date: "%B %d, %Y" }}

                            {% if post.author %}
                            <span class="ms-3">
                                <i class="fas fa-user me-1"></i>
                                {{ post.author }}
                            </span>
                            {% endif %}

                            {% if post.categories %}
                            <span class="ms-3">
                                <i class="fas fa-folder me-1"></i>
                                {% for category in post.categories %}
                                <span class="badge bg-primary me-1">{{ category }}</span>
                                {% endfor %}
                            </span>
                            {% endif %}
                        </div>

                        <p class="card-text">
                            {{ post.excerpt | strip_html | truncate: 200 }}
                        </p>

                        <div class="d-flex justify-content-between align-items-center">
                            <a href="{{ post.url | relative_url }}" class="btn btn-primary">
                                Read More <i class="fas fa-arrow-right ms-1"></i>
                            </a>

                            {% if post.tags %}
                            <div class="post-tags">
                                {% for tag in post.tags %}
                                <span class="badge bg-secondary me-1">{{ tag }}</span>
                                {% endfor %}
                            </div>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
        </article>
        {% endfor %}

        <!-- Pagination (if needed in future) -->
        {% if paginator.total_pages > 1 %}
        <nav aria-label="Blog pagination" class="mt-5">
            <ul class="pagination justify-content-center">
                {% if paginator.previous_page %}
                <li class="page-item">
                    <a class="page-link" href="{{ paginator.previous_page_path | relative_url }}">
                        <i class="fas fa-chevron-left me-1"></i>Previous
                    </a>
                </li>
                {% endif %}

                {% for page in (1..paginator.total_pages) %}
                <li class="page-item {% if page == paginator.page %}active{% endif %}">
                    <a class="page-link" href="{% if page == 1 %}{{ '/blog' | relative_url }}{% else %}{{ site.paginate_path | relative_url | replace: ':num', page }}{% endif %}">
                        {{ page }}
                    </a>
                </li>
                {% endfor %}

                {% if paginator.next_page %}
                <li class="page-item">
                    <a class="page-link" href="{{ paginator.next_page_path | relative_url }}">
                        Next <i class="fas fa-chevron-right ms-1"></i>
                    </a>
                </li>
                {% endif %}
            </ul>
        </nav>
        {% endif %}
    </div>
</div>