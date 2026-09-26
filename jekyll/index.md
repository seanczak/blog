---
layout: default
title: Topics
permalink: /
---

{% comment %}Structure, order and blurbs come from jekyll/_data/tree.yml.{% endcomment %}
<div class="archive-layout">
  <div class="topic-tree">
    {% for section in site.data.tree %}
      <section class="tree-section" id="{{ section.title | slugify }}">
        <h2 class="tree-section-title">{{ section.title }}</h2>
        {% if section.blurb %}<p class="tree-blurb">{{ section.blurb }}</p>{% endif %}
        {% for group in section.groups %}
          <details class="tree-group" id="{{ section.title | slugify }}--{{ group.title | slugify }}">
            <summary>
              <h3 class="tree-group-title">{{ group.title }}</h3>
              {% if group.blurb %}<p class="tree-blurb">{{ group.blurb }}</p>{% endif %}
            </summary>
            {% if group.posts == nil or group.posts.size == 0 %}<p class="tree-empty">Posts to come.</p>{% endif %}
            <ol class="tree-posts">
              {% for entry in group.posts %}
                {% assign post = site.posts | where: "slug", entry.slug | first %}
                {% if post %}
                  <li>
                    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
                    <p>{{ entry.blurb | default: post.description }}</p>
                  </li>
                {% else %}
                  <!-- tree.yml: no post with slug "{{ entry.slug }}" -->
                {% endif %}
              {% endfor %}
            </ol>
          </details>
        {% endfor %}
      </section>
    {% endfor %}
  </div>

  <aside class="category-nav" aria-label="Topics">
    <h2>Topics</h2>
    <nav class="category-links">
      {% for section in site.data.tree %}
        <a href="#{{ section.title | slugify }}">{{ section.title }}</a>
        {% for group in section.groups %}
          <a class="is-subtopic" href="#{{ section.title | slugify }}--{{ group.title | slugify }}">{{ group.title }}</a>
        {% endfor %}
      {% endfor %}
    </nav>
  </aside>
</div>

<script>
  (() => {
    // A sidebar link to a group expands that group before the browser scrolls to it.
    const openGroup = id => {
      const target = document.getElementById(id);
      if (target instanceof HTMLDetailsElement) target.open = true;
    };
    document.querySelectorAll('.category-links a.is-subtopic').forEach(link => {
      link.addEventListener('click', () => openGroup(link.hash.slice(1)));
    });
    if (location.hash) openGroup(decodeURIComponent(location.hash.slice(1)));
  })();
</script>
