---
layout: default
title: Writing
---

<div class="archive-layout">
  <section class="writing" aria-label="Posts">
    <ol class="post-list" id="post-list">
      {% for post in site.posts %}
        <li data-categories="{{ post.categories | join: '|' }}">
          <article class="post-card">
            {% if post.categories.size > 0 %}
              <p class="post-categories">{% for category in post.categories %}<a data-category="{{ category | slugify }}" href="#category-{{ category | slugify }}">{{ category }}</a>{% endfor %}</p>
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
    <div class="category-links">
      <button class="is-active" data-category="all" type="button">All <span>{{ site.posts | size }}</span></button>
      {% assign categories = site.categories | sort %}
      {% for category in categories %}
        <button data-category="{{ category[0] | slugify }}" type="button">{{ category[0] }} <span>{{ category[1] | size }}</span></button>
      {% endfor %}
    </div>
  </aside>
</div>

<script>
  (() => {
    const buttons = [...document.querySelectorAll('[data-category]')];
    const posts = [...document.querySelectorAll('#post-list > li')];
    const count = document.querySelector('#post-count');
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
      if (count) count.textContent = `${visible} ${visible === 1 ? 'post' : 'posts'}`;
    };

    buttons.forEach(button => button.addEventListener('click', event => {
      event.preventDefault();
      const requestedCategory = button.dataset.category;
      const category = requestedCategory !== 'all' && button.classList.contains('is-active') ? 'all' : requestedCategory;
      history.replaceState(null, '', category === 'all' ? location.pathname : `#category-${category}`);
      showCategory(category);
    }));

    const showHashCategory = () => {
      const hashCategory = location.hash.replace('#category-', '');
      showCategory(buttons.some(button => button.dataset.category === hashCategory) ? hashCategory : 'all');
    };
    window.addEventListener('hashchange', showHashCategory);
    showHashCategory();
  })();
</script>
