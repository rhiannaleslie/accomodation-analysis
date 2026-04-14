---
layout: post
title: "NLP Analysis of My Southeast Asia Accommodation Reviews"
date: 2026-04-14
author: "Rhianna Leslie"
categories: [travel, data-analysis, nlp]
tags: [accommodation, reviews, sentiment, topic-modeling, southeast-asia]
description: "An in-depth NLP analysis of accommodation comments from my 6-month Southeast Asia backpacking trip, revealing patterns in my review writing and accommodation preferences."
---

# NLP Analysis of Southeast Asia Accommodation Reviews

During my 6-month backpacking trip through Southeast Asia, I stayed at 68 different accommodations across 7 countries. This post dives deep into the linguistic patterns in my accommodation reviews using natural language processing techniques.

## The Dataset

- **Total accommodations**: 68
- **Countries visited**: Thailand, Vietnam, Indonesia, Malaysia, Cambodia, Laos, Singapore
- **Date range**: March 2025 - September 2025
- **Comments with text**: 63

## Text Preprocessing

Before analysis, I cleaned the text data by:
- Converting to lowercase
- Removing special characters and numbers
- Tokenizing into words
- Removing common stopwords
- Lemmatizing words to their base forms

## Key Findings

### Most Common Words

The most frequently mentioned words in my reviews reveal my priorities:

1. **"Lovely"** (11 mentions) - My go-to positive descriptor
2. **"Location"** (10 mentions) - Location is crucial
3. **"Basic"** (9 mentions) - Many places were described as basic
4. **"Cute"** (7 mentions) - Aesthetic appreciation
5. **"Quiet"** (6 mentions) - Peace and quiet valued
6. **"Pool"** (6 mentions) - Swimming facilities mentioned

### Topic Modeling Results

Using Latent Dirichlet Allocation (LDA), I identified 4 main topics in my comments:

**Topic 1 (38.7%)**: Beautiful views, comfort, family-friendly aspects
- Keywords: beautiful, lovely, view, bed, people, accom, comfy, free, amazing, family

**Topic 2 (33.9%)**: Location and atmosphere
- Keywords: location, quiet, pool, fab, social, fine, cute, toilet, lovely, yoga

**Topic 3 (14.5%)**: Staff and dorm experiences
- Keywords: cute, staff, lovely, dorm, stayed, clean, female, comfy, spenny, amazing

**Topic 4 (12.9%)**: Basic accommodations and social aspects
- Keywords: basic, okay, busy, lovely, family, comfy, balcony, people, met, clean

## Geographic Patterns

### Average Ratings by Country

- **Indonesia**: 4.07/5 (highest rated)
- **Thailand**: 4.0/5
- **Singapore**: 4.0/5
- **Cambodia**: 3.86/5
- **Vietnam**: 3.65/5
- **Laos**: 3.5/5
- **Malaysia**: 3.08/5 (lowest rated)

### Comment Distribution

- **Vietnam**: 16 accommodations
- **Indonesia**: 14 accommodations
- **Thailand**: 12 accommodations
- **Malaysia**: 10 accommodations
- **Cambodia**: 7 accommodations
- **Laos**: 4 accommodations

## Temporal Trends

My ratings showed interesting patterns over time:

- **March-April 2025**: Higher ratings (4.0+ average)
- **May-June 2025**: More variable ratings
- **July-August 2025**: Generally positive (3.8+ average)
- **September 2025**: Mixed ratings

## Text Length Analysis

- **Average comment length**: 3.7 words after preprocessing
- **Shortest comment**: 0 words (empty)
- **Longest comment**: 13 words

This suggests I wrote concise but meaningful reviews, focusing on key aspects rather than lengthy descriptions.

## Insights and Reflections

1. **Location matters most**: "Location" appears in 10% of my comments
2. **Atmosphere over luxury**: Words like "quiet," "cute," and "social" appear frequently
3. **Honest but positive**: My average rating of 3.72/5 shows realistic expectations
4. **Cultural adaptation**: Different countries elicited different comment patterns

## Technical Implementation

This analysis was performed using:
- **Python** with pandas, NLTK, and scikit-learn
- **Text preprocessing** with NLTK
- **Topic modeling** with Latent Dirichlet Allocation (LDA)
- **Word frequency analysis** with collections.Counter
- **Temporal analysis** with pandas datetime functions

The complete analysis code is available in the `comment-nlp-analysis.ipynb` notebook in this repository.

## Future Analysis Ideas

- **Sentiment analysis** to quantify positive/negative language
- **Geographic clustering** of accommodation types
- **Price correlation** with ratings and comments
- **Seasonal patterns** in accommodation quality

---

*This analysis provides a fascinating look at how I experienced and described accommodations during my Southeast Asia journey. The patterns reveal not just where I stayed, but how I perceived and valued different aspects of travel accommodation.*