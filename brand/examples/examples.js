const picker = document.querySelector('#theme');
picker.value = document.documentElement.dataset.theme || 'system';
picker.addEventListener('change', () => {
  if (picker.value === 'system') delete document.documentElement.dataset.theme;
  else document.documentElement.dataset.theme = picker.value;
  try { localStorage.setItem('frontier-theme', picker.value); } catch {}
});
for (const sample of document.querySelectorAll('.sample')) {
  sample.querySelectorAll('.actions button:not(:disabled)').forEach(button => button.addEventListener('click', () => {
    sample.querySelector('.demo-feedback').textContent = `${button.textContent} vald. Ingen information skickades.`;
  }));
  sample.querySelectorAll('[data-view]').forEach(button => button.addEventListener('click', () => {
    sample.querySelectorAll('[data-view]').forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    sample.querySelector('.tab-result').textContent = button.dataset.view === 'current' ? 'Aktuellt arbete: två exempel i planen.' : 'Historik: tidigare exempel finns dokumenterade.';
  }));
}
