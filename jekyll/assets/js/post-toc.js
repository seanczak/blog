// Post page: build the "On this page" table of contents from the article's headings
// and highlight the section being read. Hides the sidebar when there are no headings.
(() => {
  const layout = document.querySelector('.post-layout');
  const sidebar = document.querySelector('.article-nav');
  const toc = document.querySelector('[data-generated-toc]');
  const headings = [...document.querySelectorAll('.post h2[id], .post h3[id], .post h4[id], .post h5[id], .post h6[id]')];

  if (!layout || !sidebar || !toc || !headings.length) {
    if (sidebar) sidebar.hidden = true;
    if (layout) layout.classList.add('post-layout--plain');
    return;
  }

  const INDENT_PER_LEVEL_REM = 0.9;
  const links = new Map();
  headings.forEach(heading => {
    const link = document.createElement('a');
    const level = Number(heading.tagName.slice(1));
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent;
    link.dataset.level = level;
    link.style.setProperty('--toc-indent', `${Math.max(0, level - 2) * INDENT_PER_LEVEL_REM}rem`);
    toc.append(link);
    links.set(heading.id, link);
  });

  const setActive = id => links.forEach((link, key) => link.classList.toggle('is-active', key === id));
  setActive(headings[0].id);

  const observer = new IntersectionObserver(entries => {
    const visible = entries.filter(entry => entry.isIntersecting);
    if (visible.length) {
      const topmost = visible.sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      setActive(topmost.target.id);
    }
  }, { rootMargin: '-18% 0px -70% 0px', threshold: 0 });
  headings.forEach(heading => observer.observe(heading));
})();
