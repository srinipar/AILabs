import express from "express";
import cors from "cors";
import fetch from "node-fetch";
import dotenv from "dotenv";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

app.post("/analyze", async (req, res) => {
  const { latestMetrics, recentLogs } = req.body;

  const prompt = `
You are an AI Observability Agent for a semiconductor EDA compute farm.

Latest Metrics:
${JSON.stringify(latestMetrics, null, 2)}

Recent Logs:
${JSON.stringify(recentLogs, null, 2)}

Perform full agent workflow:

1. Detect anomaly
2. Identify root cause
3. Explain business impact
4. Recommend corrective actions
5. Generate structured ITSM ticket draft with:
   - Short Description
   - Detailed Description
   - Priority
   - Assignment Group

Respond clearly and professionally.
`;

  try {
    const response = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }],
        }),
      }
    );

    const data = await response.json();
    console.log("Gemini RAW Response:", JSON.stringify(data, null, 2));

    const text =
      data.candidates?.[0]?.content?.parts?.[0]?.text ||
      "No response from Gemini.";

    res.json({ analysis: text });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Gemini API call failed." });
  }
});

app.listen(5000, () => {
  console.log("🚀 AI Server running on port 5000");
});