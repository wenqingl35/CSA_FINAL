import { useState } from "react";

function GameTypeStep({ gameType, setGameType, nextStep }) {
  const [error, setError] = useState("");

  const handleNext = () => {
    if (!gameType) {
      setError("Please select a game type.");
      return;
    }
    nextStep();
  };

  return (
    <div>
      <h2>Select Game Type</h2>

      <select
        value={gameType}
        onChange={(e) => {
          setGameType(e.target.value);
          setError("");
        }}
      >
        <option value="">-- Choose Game Type --</option>
        <option value="NLH">No-Limit Hold'em</option>
        <option value="PLO">Pot-Limit Omaha</option>
        <option value="Mixed">Mixed Game</option>
        <option value="Other">Other</option>
      </select>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <button onClick={handleNext}>Next</button>
    </div>
  );
}

export default GameTypeStep;