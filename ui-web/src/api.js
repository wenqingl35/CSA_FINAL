const BASE_URL = "https://zany-space-computing-machine-q7g5r45jpwq9f94r4-8000.app.github.dev";
// Replace with your Codespaces URL when deploying:
// e.g. "https://<your-space>-8000.app.github.dev"

const api = {
  // -----------------------------
  // 1. Start a new hand
  // -----------------------------
  startHand: async (payload) => {
    const res = await fetch(`${BASE_URL}/hand/start`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  },

  // -----------------------------
  // 2. Update the current hand
  // -----------------------------
  updateHand: async (payload) => {
    const res = await fetch(`${BASE_URL}/hand/update`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  },

  // -----------------------------
  // 3. Get current hand analysis
  // -----------------------------
  getCurrentHand: async () => {
    const res = await fetch(`${BASE_URL}/hand/current`, {
      method: "GET"
    });
    return res.json();
  },

  // -----------------------------
  // 4. Reset the hand state
  // -----------------------------
  resetHand: async () => {
    const res = await fetch(`${BASE_URL}/hand/reset`, {
      method: "POST"
    });
    return res.json();
  },

  // -----------------------------
  // 5. One-shot analysis (optional)
  // -----------------------------
  analyzeDirect: async (payload) => {
    const res = await fetch(`${BASE_URL}/analyze`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  }
};

export default api;