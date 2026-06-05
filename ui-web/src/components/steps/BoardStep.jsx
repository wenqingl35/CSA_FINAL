import { useState } from "react";
import { formatCard } from "../../utils/cards";

function BoardStep({ board, setBoard, nextStep, prevStep }) {
  const [cardInput, setCardInput] = useState("");
  const [error, setError] = useState("");

  const addCard = () => {
    const card = formatCard(cardInput);

    if (!card) {
      setError("Invalid card format (e.g., As, Td, 7h).");
      return;
    }

    if (board.includes(card)) {
      setError("Card already on board.");
      return;
    }

    if (board.length >= 5) {
      setError("Board cannot exceed 5 cards.");
      return;
    }

    setBoard([...board, card]);
    setCardInput("");
    setError("");
  };

  const removeCard = (index) => {
    const updated = board.filter((_, i) => i !== index);
    setBoard(updated);
  };

  const handleNext = () => {
    // ⭐ Force React to commit board state before moving on
    setTimeout(() => {
      nextStep();
    }, 0);
  };

  return (
    <div>
      <h2>Board Cards</h2>

      <div style={{ marginBottom: "10px" }}>
        <input
          type="text"
          placeholder="Flop/Turn/River (e.g., As)"
          value={cardInput}
          onChange={(e) => {
            setCardInput(e.target.value);
            setError("");
          }}
        />
        <button onClick={addCard} style={{ marginLeft: "10px" }}>
          Add Card
        </button>
      </div>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <h3>Current Board:</h3>
      <ul>
        {board.map((card, index) => (
          <li key={index}>
            {card}
            <button
              style={{ marginLeft: "10px" }}
              onClick={() => removeCard(index)}
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

export default BoardStep;