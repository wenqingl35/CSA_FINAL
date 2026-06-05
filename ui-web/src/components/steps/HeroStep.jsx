import { useState } from "react";
import { parseCardInput } from "../../utils/cards";

function HeroStep({
  heroHand,
  setHeroHand,
  heroPosition,
  setHeroPosition,
  heroStack,
  setHeroStack,
  potSize,
  setPotSize,
  nextStep,
  prevStep
}) {
  const [handInput, setHandInput] = useState("");
  const [error, setError] = useState("");

  const handleNext = () => {
    const cards = parseCardInput(handInput);

    if (cards.length !== 2) {
      setError("Enter exactly 2 valid cards (e.g., As Kd).");
      return;
    }

    setHeroHand(cards);

    // Flush state before moving forward
    setTimeout(() => {
      nextStep();
    }, 0);
  };

  return (
    <div>
      <h2>Hero Info</h2>

      <div>
        <label>Hero Hand:</label>
        <input
          type="text"
          placeholder="As Kd"
          value={handInput}
          onChange={(e) => {
            setHandInput(e.target.value);
            setError("");
          }}
        />
      </div>

      <div>
        <label>Position:</label>
        <input
          type="text"
          value={heroPosition}
          onChange={(e) => setHeroPosition(e.target.value)}
        />
      </div>

      <div>
        <label>Hero Stack:</label>
        <input
          type="number"
          value={heroStack}
          onChange={(e) => setHeroStack(Number(e.target.value))}
        />
      </div>

      <div>
        <label>Pot Size:</label>
        <input
          type="number"
          value={potSize}
          onChange={(e) => setPotSize(Number(e.target.value))}
        />
      </div>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <button onClick={prevStep}>Back</button>
      <button onClick={handleNext} style={{ marginLeft: "10px" }}>
        Next
      </button>
    </div>
  );
}

export default HeroStep;