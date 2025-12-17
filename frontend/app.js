async function loadStatus() {
  const el = document.getElementById("status");
  el.textContent = "Loading status from Azure Function...";

  try {
    const res = await fetch("/api/status");
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();

    el.innerHTML = `
      <div><b>App:</b> ${data.app}</div>
      <div><b>Env:</b> ${data.environment}</div>
      <div><b>Version:</b> ${data.version}</div>
      <div><b>Last Updated:</b> ${data.lastUpdated}</div>
      <div style="margin-top:12px;"><b>Messages:</b></div>
      <ul>
        ${data.messages.map(m => `<li>${m}</li>`).join("")}
      </ul>
    `;
  } catch (err) {
    el.textContent = "Failed to load status ❌ " + err.message;
  }
}

loadStatus();
