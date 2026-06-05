import { useState, useEffect } from "react";

function AnalysisStep({ prevStep }) {
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchAnalysis = async () => {
      try {
        const res = await fetch(
          "https://zany-space-computing-machine-q7g5r45jpwq9f94r4-8000.app.github.dev/hand/current"
        );

        if (!res.ok) {
          throw new Error(`Backend error: ${res.status}`);
        }

        const data = await res.json();

        if (!data || data.error) {
          setError(data.error || "Unknown backend error");
          setLoading(false);
          return;
        }

        setAnalysis(data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    // ⭐ Ensure React flushes state before fetching
    setTimeout(fetchAnalysis, 0);
  }, []);

  if (loading) {
    return (
      <div>
        <h2>Analyzing Hand...</h2>
        <p>Please wait while the solver evaluates the spot.</p>
      </div>
    );
  }

  if (error) {
    return (
      <div>
        <h2>Analysis Error</h2>
        <p style={{ color: "red" }}>{error}</p>
        <button onClick={prevStep}>Back</button>
      </div>
    );
  }

  return (
    <div>
      <h2>Hand Analysis</h2>

      <h3>Equity Estimate</h3>
      <p>{analysis.equity ? `${analysis.equity}%` : "N/A"}</p>

      <h3>Hand Summary</h3>
      <pre style={{ background: "#eee", padding: "10px" }}>
        {JSON.stringify(analysis.hand, null, 2)}
      </pre>

      <h3>Solver Output</h3>
      <pre style={{ background: "#eee", padding: "10px" }}>
        {JSON.stringify(analysis.solver_output, null, 2)}
      </pre>

      <button onClick={prevStep} style={{ marginTop: "20px" }}>
        Back
      </button>
    </div>
  );
}

export default AnalysisStep;