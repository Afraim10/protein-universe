const filters = document.querySelector('.filters');
const cards = [...document.querySelectorAll('.poster-card')];
if (filters) {
  filters.hidden = false;
  filters.addEventListener('click', event => {
    const button = event.target.closest('button[data-filter]');
    if (!button) return;
    filters.querySelectorAll('button').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    cards.forEach(card => { card.hidden = button.dataset.filter !== 'All' && card.dataset.category !== button.dataset.filter; });
    const count = cards.filter(card => !card.hidden).length;
    document.querySelector('#result-count').textContent = `${count} ${count === 1 ? 'poster' : 'posters'} shown`;
  });
}
