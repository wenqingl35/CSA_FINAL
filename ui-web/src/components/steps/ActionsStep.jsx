import { useState } from "react";
import { parseCardInput } from "../../utils/cards";

function ActionsStep({ actionHistory, setActionHistory, nextStep, prevStep }) {
  const [player, setPlayer] = useState("");
  const [action, setAction] = useState("");
  const [amount, setAmount] = useState("");
  const [error, setError] = useState("");

  const addAction = () => {
    if (!player || !action) {
      setError("Player and action are required.");
      return;
    }

    const newAction = {
      player,
      action,
      amount: amount ? parseFloat(amount) : null
    };

    setActionHistory([...actionHistory, newAction]);

    setPlayer("");
    setAction("");
    setAmount("");
    setError("");
  };

  const removeAction = (index) => {
    const updated = actionHistory.filter((_, i) => i !== index);
    setActionHistory(updated);
  };

  const handleNext = () => {
    // ⭐ Force React to commit actionHistory before moving on
    setTimeout(() => {
      nextStep();
    }, 0);
  };

  return (
    <div>
      <h2>Actions</h2>

      <div style={{ marginBottom: "10px" }}>
        <label>Player:</label>
        <input
          type="text"
          value={player}
          placeholder="Hero, Villain1"
          onChange={(e) => {
            setPlayer(e.target.value);
            setError("");
          }}
        />
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Action:</label>
        <input
          type="text"
          value={action}
          placeholder="bet, call, fold, raise"
          onChange={(e) => {
            setAction(e.target.value);
            setError("");
          }}
        />
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Amount (optional):</label>
        <input
          type="number"
          value={amount}
          placeholder="50"
          onChange={(e) => setAmount(e.target.value)}
        />
      </div>

      <button onClick={addAction}>Add Action</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <h3>Action History:</h3>
      <ul>
        {actionHistory.map((act, index) => (
          <li key={index}>
            {act.player} — {act.action}
            {act.amount !== null ? ` (${act.amount})` : ""}
            <button
              style={{ marginLeft: "10px" }}
              onClick={() => removeAction(index)}
            >
              Remove
            </button>
          </li>
        ))}
      </ul>

      <div style={{ marginTop: "20px" }}>
        <button onClick={prevStep}>Back</button>
        <button onClick={handleNext} style={{ marginLeft: "10px" }}>
          Next
        </button>
      </div>
    </div>
  );
}

export default ActionsStep;