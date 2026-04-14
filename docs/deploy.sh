#!/bin/bash

# GitHub Pages Deployment Script for Accommodation Analysis
# This script builds and deploys the Jekyll site to GitHub Pages

set -e  # Exit on any error

echo "🚀 Starting GitHub Pages deployment..."

# Check if we're in the right directory
if [ ! -d "docs" ]; then
    echo "❌ Error: docs directory not found. Run this script from the project root."
    exit 1
fi

# Check if Jekyll is installed
if ! command -v jekyll &> /dev/null; then
    echo "⚠️  Jekyll not found. Installing Jekyll..."
    gem install jekyll bundler
fi

# Navigate to docs directory
cd docs

# Install dependencies if Gemfile exists
if [ -f "Gemfile" ]; then
    echo "📦 Installing Ruby dependencies..."
    bundle install
fi

# Build the site
echo "🔨 Building Jekyll site..."
jekyll build

# Check if build was successful
if [ ! -d "_site" ]; then
    echo "❌ Error: Jekyll build failed. Check for errors above."
    exit 1
fi

# Go back to project root
cd ..

# Check if this is a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not a git repository. Initialize git first."
    exit 1
fi

# Check if remote origin exists
if ! git remote get-url origin &> /dev/null; then
    echo "❌ Error: No remote origin found. Set up your GitHub repository first."
    echo "Run: git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    exit 1
fi

# Add and commit changes
echo "📝 Committing changes..."
git add .
git commit -m "Deploy to GitHub Pages" || echo "⚠️  No changes to commit"

# Deploy to GitHub Pages
echo "🚀 Deploying to GitHub Pages..."
git subtree push --prefix docs/_site origin gh-pages || {
    echo "❌ Subtree push failed. Trying force push..."
    git push origin `git subtree split --prefix docs/_site`:gh-pages --force
}

echo "✅ Deployment complete!"
echo "🌐 Your site should be available at: https://YOUR_USERNAME.github.io/YOUR_REPO/"
echo "Note: Replace YOUR_USERNAME and YOUR_REPO with your actual GitHub details"