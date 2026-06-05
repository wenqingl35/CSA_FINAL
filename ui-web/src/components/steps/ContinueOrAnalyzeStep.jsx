function ContinueOrAnalyzeStep({ nextStep, analyzeStep, prevStep }) {
  const handleContinue = () => {
    // ⭐ Ensure React flushes any pending state updates
    setTimeout(() => {
      nextStep();
    }, 0);
  };

  const handleAnalyze = () => {
    // ⭐ Same flush for analysis path
    setTimeout(() => {
      analyzeStep();
    }, 0);
  };

  return (
    <div>
      <h2>Next Action</h2>
      <p>
        You can continue updating the hand (add more board cards or actions),
        or analyze the current spot using the solver.
      </p>

      <div style={{ marginTop: "20px" }}>
        <button onClick={prevStep} style={{ marginRight: "10px" }}>
          Back
        </button>

        <button
          onClick={handleContinue}
          style={{ marginRight: "10px", backgroundColor: "#4CAF50", color: "white" }}
        >
          Continue Updating Hand
        </button>

        <button
          onClick={handleAnalyze}
          style={{ backgroundColor: "#2196F3", color: "white" }}
        >
          Analyze Now
        </button>
      </div>
    </div>
  );
}

export default ContinueOrAnalyzeStep;