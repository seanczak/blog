---
layout: default
title: Home
---

# Writing

Notes, experiments, and things worth remembering.

<ul class="post-list">
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a><br>
      <span class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</span>
      {% if post.description %}<div>{{ post.description }}</div>{% endif %}
    </li>
  {% endfor %}
</ul>
