async function loadStatus() {
  const el = document.getElementById("status");
  el.textContent = "Loading application status...";

  try {
    const res = await fetch("/api/status", { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();

    el.innerHTML = `
      <div><b>App:</b> ${data.app}</div>
      <div><b>Env:</b> ${data.environment}</div>
      <div><b>Version:</b> ${data.version}</div>
      <div><b>Last Updated:</b> ${data.lastUpdated}</div>
      <div style="margin-top:10px;"><b>Messages:</b></div>
      <ul>${data.messages.map(m => `<li>${m}</li>`).join("")}</ul>
    `;
  } catch (err) {
    el.textContent = "Failed to load status ❌ " + err.message;
  }
}

async function loadMetrics() {
  const el = document.getElementById("metrics");
  el.textContent = "Loading runtime metrics...";

  try {
    const res = await fetch("/api/metrics", { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();

    el.innerHTML = `
      <div><b>Request ID:</b> ${data.requestId}</div>
      <div><b>Timestamp (UTC):</b> ${data.timestampUtc}</div>
      <div><b>Version:</b> ${data.build.version}</div>
      <div><b>Commit:</b> ${data.build.commitSha}</div>
      <div><b>Uptime (s):</b> ${data.runtime.uptimeSeconds}</div>
    `;
  } catch (err) {
    el.textContent = "Failed to load metrics ❌ " + err.message;
  }
}

document.getElementById("refreshBtn").addEventListener("click", () => {
  loadStatus();
  loadMetrics();
});

loadStatus();
loadMetrics();
