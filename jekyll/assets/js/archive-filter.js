// Archive: filter the post list by category from the sidebar buttons, the category
// pills on each post, or the phone-width <select>. The choice is kept in the URL
// as #category-<slug>, so a post's category pill can link straight to a filtered view.
(() => {
  const HASH_PREFIX = '#category-';
  const ALL = 'all';
  const controls = [...document.querySelectorAll('[data-category]')];
  const posts = [...document.querySelectorAll('#post-list > li')];
  const select = document.querySelector('#category-select');

  const slugify = value => value.toLowerCase().trim().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
  const isKnown = category => controls.some(control => control.dataset.category === category);

  const showCategory = category => {
    let isFirstVisible = true;
    posts.forEach(post => {
      const postCategories = (post.dataset.categories || '').split('|').map(slugify);
      const matches = category === ALL || postCategories.includes(category);
      post.hidden = !matches;
      // Explicit class rather than :first-child, which ignores hidden rows.
      post.classList.toggle('is-first-visible', matches && isFirstVisible);
      if (matches) isFirstVisible = false;
    });
    controls.forEach(control => control.classList.toggle('is-active', control.dataset.category === category));
    if (select) select.value = category;
  };

  const selectCategory = category => {
    history.replaceState(null, '', category === ALL ? location.pathname : `${HASH_PREFIX}${category}`);
    showCategory(category);
  };

  controls.forEach(control => control.addEventListener('click', event => {
    event.preventDefault();
    const requested = control.dataset.category;
    // Clicking the active category again clears the filter.
    selectCategory(requested !== ALL && control.classList.contains('is-active') ? ALL : requested);
  }));
  select?.addEventListener('change', () => selectCategory(select.value));

  const showCategoryFromHash = () => {
    const requested = location.hash.replace(HASH_PREFIX, '');
    showCategory(isKnown(requested) ? requested : ALL);
  };
  window.addEventListener('hashchange', showCategoryFromHash);
  showCategoryFromHash();
})();
