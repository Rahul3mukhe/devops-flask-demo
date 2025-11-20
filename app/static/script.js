async function loadData(q="") {
  let url = "/items";
  if (q) url = "/items?q=" + encodeURIComponent(q);
  const items = await fetch(url).then(r => r.json());
  const version = await fetch("/version").then(r => r.json()).catch(_=>({version:"-"}));
  const health = await fetch("/health").then(r => r.json()).catch(_=>({status:"?"}));

  document.getElementById("count-items").innerText = items.length;
  document.getElementById("ver-badge").innerText = version.version;
  document.getElementById("health-badge").innerText = health.status;

  const tbody = document.getElementById("items-table");
  tbody.innerHTML = items.map(i => `
    <tr>
      <td>${i.id}</td>
      <td>${escapeHtml(i.name)}</td>
      <td>${escapeHtml(i.description)}</td>
      <td>${new Date(i.created_at).toLocaleString()}</td>
      <td>
        <button class="btn btn-sm btn-danger" onclick="remove(${i.id})">Delete</button>
      </td>
    </tr>
  `).join("");
}

function escapeHtml(s) { return (s || "").replace(/&/g,'&amp;').replace(/</g,'&lt;'); }

async function submitAdd(e) {
  e.preventDefault();
  const name = document.getElementById("name").value.trim();
  const desc = document.getElementById("desc").value.trim();
  if (!name) return;
  await fetch("/items", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, description: desc })
  });
  document.getElementById("add-form").reset();
  loadData();
}

async function remove(id) {
  if (!confirm("Delete item " + id + "?")) return;
  await fetch("/items/" + id, { method: "DELETE" });
  loadData();
}

let timer = null;
function search() {
  clearTimeout(timer);
  timer = setTimeout(()=> {
    const q = document.getElementById("search").value.trim();
    loadData(q);
  }, 300);
}

// initial
loadData();
