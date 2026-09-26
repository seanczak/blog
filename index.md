---
layout: default
title: Writing
---

<div class="archive-layout">
  <section class="writing" aria-label="Posts">
    <ol class="post-list" id="post-list">
      {% for post in site.posts %}
        {% capture post_categories %}{% include post-categories.html post=post %}{% endcapture %}
        {% assign post_categories = post_categories | split: '|' %}
        <li data-categories="{{ post_categories | join: '|' }}">
          <article class="post-card">
            {% if post_categories.size > 0 %}
              <p class="post-categories">{% for category in post_categories %}<a data-category="{{ category | slugify }}" href="#category-{{ category | slugify }}">{{ category }}</a>{% endfor %}</p>
            {% endif %}
            <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
            {% if post.description %}<p>{{ post.description }}</p>{% endif %}
            <p class="post-meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time></p>
          </article>
        </li>
      {% endfor %}
    </ol>
  </section>

  <aside class="category-nav" aria-label="Post categories">
    <h2>Categories</h2>
    <label class="visually-hidden" for="category-select">Filter posts by category</label>
    {% comment %}Built from post-categories.html rather than site.categories so directory-derived categories are excluded.{% endcomment %}
    {% assign joined_categories = '' %}
    {% for post in site.posts %}
      {% capture post_categories %}{% include post-categories.html post=post %}{% endcapture %}
      {% assign joined_categories = joined_categories | append: post_categories | append: '|' %}
    {% endfor %}
    {% assign category_occurrences = joined_categories | split: '|' %}
    {% assign categories = category_occurrences | uniq | sort %}
    <select class="category-select" id="category-select">
      <option value="all">All ({{ site.posts | size }})</option>
      {% for category in categories %}
        {% assign category_count = category_occurrences | where_exp: 'item', 'item == category' | size %}
        <option value="{{ category | slugify }}">{{ category }} ({{ category_count }})</option>
      {% endfor %}
    </select>
    <div class="category-links">
      <button class="is-active" data-category="all" type="button">All <span>{{ site.posts | size }}</span></button>
      {% for category in categories %}
        {% assign category_count = category_occurrences | where_exp: 'item', 'item == category' | size %}
        <button data-category="{{ category | slugify }}" type="button">{{ category }} <span>{{ category_count }}</span></button>
      {% endfor %}
    </div>
  </aside>
</div>

<script>
  (() => {
    const buttons = [...document.querySelectorAll('[data-category]')];
    const posts = [...document.querySelectorAll('#post-list > li')];
    const count = document.querySelector('#post-count');
    const categorySelect = document.querySelector('#category-select');
    const slugify = value => value.toLowerCase().trim().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');

    const showCategory = category => {
      let visible = 0;
      let firstVisible = true;
      posts.forEach(post => {
        const categories = (post.dataset.categories || '').split('|').map(slugify);
        const matches = category === 'all' || categories.includes(category);
        post.hidden = !matches;
        post.classList.toggle('is-first-visible', matches && firstVisible);
        if (matches) {
          visible += 1;
          firstVisible = false;
        }
      });
      buttons.forEach(button => button.classList.toggle('is-active', button.dataset.category === category));
      if (categorySelect) categorySelect.value = category;
      if (count) count.textContent = `${visible} ${visible === 1 ? 'post' : 'posts'}`;
    };

    buttons.forEach(button => button.addEventListener('click', event => {
      event.preventDefault();
      const requestedCategory = button.dataset.category;
      const category = requestedCategory !== 'all' && button.classList.contains('is-active') ? 'all' : requestedCategory;
      history.replaceState(null, '', category === 'all' ? location.pathname : `#category-${category}`);
      showCategory(category);
    }));
    categorySelect?.addEventListener('change', () => {
      const category = categorySelect.value;
      history.replaceState(null, '', category === 'all' ? location.pathname : `#category-${category}`);
      showCategory(category);
    });

    const showHashCategory = () => {
      const hashCategory = location.hash.replace('#category-', '');
      showCategory(buttons.some(button => button.dataset.category === hashCategory) ? hashCategory : 'all');
    };
    window.addEventListener('hashchange', showHashCategory);
    showHashCategory();
  })();
</script>
