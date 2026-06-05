import { useState } from "react";

import HeroStep from "./components/steps/HeroStep";
import BoardStep from "./components/steps/BoardStep";
import OpponentsStep from "./components/steps/OpponentsStep";
import ActionsStep from "./components/steps/ActionsStep";
import ContinueOrAnalyzeStep from "./components/steps/ContinueOrAnalyzeStep";
import AnalysisStep from "./components/steps/AnalysisStep";

function App() {
  const [step, setStep] = useState(0);

  // Global state for the hand
  const [heroHand, setHeroHand] = useState([]);
  const [heroPosition, setHeroPosition] = useState("");
  const [heroStack, setHeroStack] = useState(0);
  const [potSize, setPotSize] = useState(0);

  const [board, setBoard] = useState([]);
  const [opponents, setOpponents] = useState([]);
  const [actionHistory, setActionHistory] = useState([]);

  const nextStep = () => setStep((s) => s + 1);
  const prevStep = () => setStep((s) => Math.max(0, s - 1));

  const startHand = async () => {
    const payload = {
      game_type: "NLHE",
      hero_hand: heroHand,
      board: board,
      hero_position: heroPosition,
      hero_stack: heroStack,
      pot_size: potSize,
      action_history: actionHistory,
      opponents: opponents
    };

    console.log("START PAYLOAD:", payload);

    try {
      const res = await fetch(
        "https://zany-space-computing-machine-q7g5r45jpwq9f94r4-8000.app.github.dev/hand/start",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        }
      );

      const data = await res.json();
      console.log("START RESPONSE:", data);
    } catch (err) {
      console.error("START ERROR:", err);
    }
  };

  const analyzeStep = () => {
    setStep(5);
  };

  return (
    <div style={{ padding: "20px" }}>
      {step === 0 && (
        <HeroStep
          heroHand={heroHand}
          setHeroHand={setHeroHand}
          heroPosition={heroPosition}
          setHeroPosition={setHeroPosition}
          heroStack={heroStack}
          setHeroStack={setHeroStack}
          potSize={potSize}
          setPotSize={setPotSize}
          nextStep={nextStep}
          prevStep={prevStep}
        />
      )}

      {step === 1 && (
        <BoardStep
          board={board}
          setBoard={setBoard}
          nextStep={nextStep}
          prevStep={prevStep}
        />
      )}

      {step === 2 && (
        <OpponentsStep
          opponents={opponents}
          setOpponents={setOpponents}
          nextStep={nextStep}
          prevStep={prevStep}
        />
      )}

      {step === 3 && (
        <ActionsStep
          actionHistory={actionHistory}
          setActionHistory={setActionHistory}
          nextStep={nextStep}
          prevStep={prevStep}
        />
      )}

      {step === 4 && (
        <ContinueOrAnalyzeStep
          nextStep={() => {
            startHand();
            nextStep();
          }}
          analyzeStep={() => {
            startHand();
            analyzeStep();
          }}
          prevStep={prevStep}
        />
      )}

      {step === 5 && <AnalysisStep prevStep={prevStep} />}
    </div>
  );
}

export default App;