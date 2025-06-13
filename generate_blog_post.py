#!/usr/bin/env python3
import os
from datetime import date

title = input("Post Title: ").strip()
description = input("Post Description: ").strip()
tags = input("Tags (comma-separated): ").strip()
slug = title.lower().replace(" ", "_").replace("-", "_")
pub_date = date.today().isoformat()

intro = input("Intro paragraph (or leave blank to add later): ").strip()

content = f"""---
title: "{title}"
description: "{description}"
pubDate: {pub_date}
tags: [{', '.join([f'"{t.strip()}"' for t in tags.split(',') if t.strip()])}]
---

{intro or 'Start writing your content here.'}
"""

folder = "src/content/blog"
filename = f"{slug}.md"
filepath = os.path.join(folder, filename)

os.makedirs(folder, exist_ok=True)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Blog post created: {filepath}")
