import { useState } from "react";

function OpponentsStep({ opponents, setOpponents, nextStep, prevStep }) {
  const [name, setName] = useState("");
  const [position, setPosition] = useState("");
  const [stack, setStack] = useState("");
  const [notes, setNotes] = useState("");
  const [error, setError] = useState("");

  const addOpponent = () => {
    if (!name || !position || !stack) {
      setError("Name, position, and stack are required.");
      return;
    }

    const newOpponent = {
      name,
      position,
      stack: parseFloat(stack),
      notes: notes || "None"
    };

    setOpponents([...opponents, newOpponent]);

    setName("");
    setPosition("");
    setStack("");
    setNotes("");
    setError("");
  };

  const removeOpponent = (index) => {
    const updated = opponents.filter((_, i) => i !== index);
    setOpponents(updated);
  };

  const handleNext = () => {
    // ⭐ Force React to commit opponents state before moving on
    setTimeout(() => {
      nextStep();
    }, 0);
  };

  return (
    <div>
      <h2>Opponents</h2>

      <div style={{ marginBottom: "10px" }}>
        <label>Opponent Name:</label>
        <input
          type="text"
          value={name}
          placeholder="Villain1"
          onChange={(e) => {
            setName(e.target.value);
            setError("");
          }}
        />
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Position:</label>
        <input
          type="text"
          value={position}
          placeholder="BB, UTG, CO"
          onChange={(e) => {
            setPosition(e.target.value);
            setError("");
          }}
        />
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Stack (bb):</label>
        <input
          type="number"
          value={stack}
          placeholder="100"
          onChange={(e) => {
            setStack(e.target.value);
            setError("");
          }}
        />
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Notes (optional):</label>
        <input
          type="text"
          value={notes}
          placeholder="loose, aggressive"
          onChange={(e) => setNotes(e.target.value)}
        />
      </div>

      <button onClick={addOpponent}>Add Opponent</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <h3>Current Opponents:</h3>
      <ul>
        {opponents.map((op, index) => (
          <li key={index}>
            {op.name} — {op.position} — {op.stack}bb — {op.notes}
            <button
              style={{ marginLeft: "10px" }}
              onClick={() => removeOpponent(index)}
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

export default OpponentsStep;