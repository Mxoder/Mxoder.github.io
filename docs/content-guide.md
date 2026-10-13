# Updating the homepage

The site uses Jekyll and keeps the original academic homepage styling.

## Pages

- `/`: personal biography and statistics badges only.
- `/news/`: all news entries from `_data/news.yml`, in file order (newest first).
- `/publications/`: all publications rendered by `_includes/content/publications.md`.
- `/projects/`: projects from `_includes/content/projects.md`.
- `/blog/`: published local articles, newest first, followed by the existing Zhihu links.

Edit the individual publication files under `_includes/content/` to update a paper.
Add a paper include to `publications.md` to include it in the full list. Update
external writing links in `_includes/content/blogs.md`. The previous education,
awards, internship and academic service content is preserved in
`_includes/content/background.md` for future use; it is not displayed on the homepage.
Navigation is defined in `_data/navigation.yml`.

## Adding a local blog article

Create a file under `_posts/` named `YYYY-MM-DD-article-slug.md`, for example
`2026-10-13-lora-from-scratch.md`:

```markdown
---
title: "LoRA from Scratch"
description: "A short description for the blog listing."
tags: [LLM, LoRA]
---

Write the article here in Markdown.
```

Jekyll automatically uses the shared `post` layout, generates
`/blog/lora-from-scratch/`, and adds the article to `/blog/`. The list uses the
article title, date, and optional description. No manual navigation or list edits
are needed. Future-dated posts stay hidden until their publication date; use
`published: false` for unpublished content.

For a deeper URL, add an explicit permalink to the article's front matter:

```yaml
permalink: /blog/llm/lora-from-scratch/
```

This changes the article URL; it does not create an index at `/blog/llm/`.
Use unique slugs or permalinks to prevent articles from overwriting one another.

Use `relative_url` for internal links and images so assets load on nested pages:

```liquid
[Publications]({{ '/publications/' | relative_url }})
![Diagram]({{ '/images/diagram.png' | relative_url }})
```

## Preview

With the repository's Ruby dependencies installed:

```sh
bundle exec jekyll serve
```

Open `http://localhost:4000/` and the four section URLs. Restart Jekyll after
changing `_config.yml`. Content-only changes reload during the development server.
