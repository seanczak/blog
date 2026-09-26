// Landing page: collapsible topic groups.
// - Sidebar buttons scroll to a section or group (expanding a group) without changing the URL.
// - Only one group is open at a time. `name` on <details> does this natively in current
//   browsers; this covers older ones.
// - An incoming /#<id> link (e.g. from a post) opens that group.
(() => {
  const groups = [...document.querySelectorAll('.tree-group')];

  const openTarget = id => {
    const target = document.getElementById(id);
    if (target instanceof HTMLDetailsElement) target.open = true;
    return target;
  };

  const closeOthers = openGroup => {
    groups.forEach(group => { if (group !== openGroup) group.open = false; });
  };

  groups.forEach(group => group.addEventListener('toggle', () => {
    if (group.open) closeOthers(group);
  }));

  // Respect the visitor's reduced-motion setting.
  const scrollBehavior = () => (matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth');

  document.querySelectorAll('.category-links button[data-target]').forEach(button => {
    button.addEventListener('click', () => {
      openTarget(button.dataset.target)?.scrollIntoView({ behavior: scrollBehavior(), block: 'start' });
    });
  });

  if (location.hash) openTarget(decodeURIComponent(location.hash.slice(1)));
})();
