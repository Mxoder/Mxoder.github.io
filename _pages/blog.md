---
permalink: /blog/
title: "Blog"
excerpt: "Technical writing and Chinese-language articles on Zhihu."
---

# ✍️ Blog

{% if site.posts.size > 0 %}
## Articles

<ul class="post-list">
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
    <span class="post-list__date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y.%m.%d' }}</time></span>
    {% if post.description %}<p>{{ post.description | escape }}</p>{% endif %}
  </li>
{% endfor %}
</ul>

## Writing on Zhihu
{% endif %}

{% include content/blogs.md %}
