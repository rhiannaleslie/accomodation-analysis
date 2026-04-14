#!/bin/bash

# Script to create a new blog post template
# Usage: ./new_post.sh "Post Title" [category1,category2] [tag1,tag2]

if [ $# -lt 1 ]; then
    echo "Usage: $0 \"Post Title\" [categories] [tags]"
    echo "Example: $0 \"My Travel Analysis\" \"travel,data\" \"analysis,charts\""
    exit 1
fi

TITLE="$1"
CATEGORIES="${2:-uncategorized}"
TAGS="${3:-blog}"
DATE=$(date +%Y-%m-%d)
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//' | sed 's/-$//')
FILENAME="${DATE}-${SLUG}.md"

cat > "docs/_posts/${FILENAME}" << EOF
---
layout: post
title: "${TITLE}"
date: ${DATE}
author: "Rhianna Leslie"
categories: [${CATEGORIES}]
tags: [${TAGS}]
description: "Add a brief description of your post here"
---

# ${TITLE}

## Introduction

Write your blog post content here. Use Markdown formatting for headers, lists, links, and code blocks.

## Analysis Section

Add your data analysis, charts, or insights here.

## Conclusion

Summarize your findings and key takeaways.

## Technical Details

Include any technical information about your analysis methods, tools used, or code snippets.

\`\`\`python
# Example code block
print("Hello, World!")
\`\`\`

---

*This post is part of the Southeast Asia Accommodation Analysis series.*
EOF

echo "✅ Created new blog post: docs/_posts/${FILENAME}"
echo "📝 Edit the file to add your content and update the description"