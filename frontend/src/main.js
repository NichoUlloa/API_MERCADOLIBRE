const form = document.createElement('form');
form.innerHTML = `
  <input id="q" placeholder="search" />
  <button>Go</button>
`;
const results = document.createElement('div');

document.getElementById('app').append(form, results);

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const q = document.getElementById('q').value;
  const res = await fetch(`/search?q=${encodeURIComponent(q)}`);
  const data = await res.json();
  results.textContent = JSON.stringify(data, null, 2);
});
