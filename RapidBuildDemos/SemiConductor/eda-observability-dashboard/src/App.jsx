import React, { useState, useEffect, useCallback } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import Papa from "papaparse";

function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedHost, setSelectedHost] = useState("");
  const [cpuMemoryData, setCpuMemoryData] = useState([]);
  const [diskNfsErrorData, setDiskNfsErrorData] = useState([]);
  const [anomaly, setAnomaly] = useState(null);
  const [allHosts, setAllHosts] = useState([]);

  //Phase 2 for Logs
  const [analysis, setAnalysis] = useState("");
  const [logs, setLogs] = useState([]);

  const parseCSV = useCallback(() => {
  setLoading(true);

  // Load metrics
  Papa.parse("/metrics.csv", {
    download: true,
    header: true,
    dynamicTyping: true,
    skipEmptyLines: true,
    complete: (results) => {
      setData(results.data);
      setLoading(false);
    },
    error: (err) => {
      setError(err.message);
      setLoading(false);
    },
  });

  // Load logs
  Papa.parse("/logs.csv", {
    download: true,
    header: true,
    dynamicTyping: true,
    skipEmptyLines: true,
    complete: (results) => {
      setLogs(results.data);
    },
    error: (err) => {
      console.error("Error loading logs.csv:", err);
    },
  });

}, []);

  useEffect(() => {
    parseCSV();
  }, [parseCSV]);

  useEffect(() => {
    if (data.length > 0) {
      const hosts = [...new Set(data.map((item) => item.host))];
      setAllHosts(hosts);
      setSelectedHost(hosts[0] || "");
    }
  }, [data]);

  useEffect(() => {
    if (selectedHost) {
      const filteredData = data.filter(
        (item) => item.host === selectedHost
      );

      setCpuMemoryData(
        filteredData.map((item) => ({
          time: new Date(item.timestamp).toLocaleTimeString(),
          cpu_percent: item.cpu_percent,
          memory_percent: item.memory_percent,
        }))
      );

      setDiskNfsErrorData(
        filteredData.map((item) => ({
          time: new Date(item.timestamp).toLocaleTimeString(),
          disk_io_mb_s: item.disk_io_mb_s,
          nfs_latency_ms: item.nfs_latency_ms,
          error_rate_percent: item.error_rate_percent,
        }))
      );
    }
  }, [selectedHost, data]);

  useEffect(() => {
    const latestCpu =
      cpuMemoryData.length > 0
        ? cpuMemoryData[cpuMemoryData.length - 1].cpu_percent
        : 0;

    const latestNfs =
      diskNfsErrorData.length > 0
        ? diskNfsErrorData[diskNfsErrorData.length - 1].nfs_latency_ms
        : 0;

    if (latestCpu > 90) {
      setAnomaly(`High CPU Usage (${latestCpu}%) on ${selectedHost}`);
    } else if (latestNfs > 100) {
      setAnomaly(`High NFS Latency (${latestNfs}ms) on ${selectedHost}`);
    } else {
      setAnomaly(null);
    }
  }, [cpuMemoryData, diskNfsErrorData, selectedHost]);
const handleAnalyze = async () => {
  setAnalysis("AI analyzing anomaly...");

  const latestMetrics = {
    cpu: latestCpu,
    nfs_latency: latestNfs,
    error_rate: latestError,
    host: selectedHost,
  };

  const recentLogs = logs.filter(
    (log) => log.host === selectedHost
  );

  try {
    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        latestMetrics,
        recentLogs,
      }),
    });

    const data = await response.json();
    setAnalysis(data.analysis);
  } catch (err) {
    setAnalysis("Error contacting AI server.");
  }
};
  const latestCpu =
    cpuMemoryData.length > 0
      ? cpuMemoryData[cpuMemoryData.length - 1].cpu_percent
      : 0;

  const latestNfs =
    diskNfsErrorData.length > 0
      ? diskNfsErrorData[diskNfsErrorData.length - 1].nfs_latency_ms
      : 0;

  const latestError =
    diskNfsErrorData.length > 0
      ? diskNfsErrorData[diskNfsErrorData.length - 1].error_rate_percent
      : 0;

  if (loading) {
    return <div style={{ padding: 50 }}>Loading...</div>;
  }

  if (error) {
    return <div style={{ padding: 50, color: "red" }}>Error: {error}</div>;
  }

  return (
  <div
  style={{
    background: "#0f172a",
    color: "white",
    minHeight: "100vh",
    padding: "40px",
  }}
>
  <div style={{ maxWidth: "1300px", margin: "0 auto" }}>
        {/* Anomaly Banner */}
        {anomaly && (
          <div
            style={{
              background: "#dc2626",
              padding: "15px",
              borderRadius: "8px",
              marginBottom: "20px",
              fontWeight: "bold",
              textAlign: "center",
            }}
          >
            🚨 {anomaly}
          </div>
        )}

        {/* Header */}
        <h1
          style={{
            fontSize: "32px",
            marginBottom: "20px",
            fontWeight: "bold",
          }}
        >
          Semiconductor EDA Compute Farm Observability
        </h1>

        {/* Host Selector */}
        <div style={{ marginBottom: "30px" }}>
          <label style={{ marginRight: "10px" }}>Select Host:</label>
          <select
            value={selectedHost}
            onChange={(e) => setSelectedHost(e.target.value)}
            style={{
              padding: "8px",
              borderRadius: "6px",
              background: "#1e293b",
              color: "white",
              border: "1px solid #334155",
            }}
          >
            {allHosts.map((host) => (
              <option key={host} value={host}>
                {host}
              </option>
            ))}
          </select>
        </div>

        {/* KPI Cards */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(4, 1fr)",
            gap: "20px",
            marginBottom: "30px",
          }}
        >
          {[
            { label: "CPU Usage", value: `${latestCpu}%` },
            { label: "NFS Latency", value: `${latestNfs} ms` },
            { label: "Error Rate", value: `${latestError}%` },
            { label: "Node Health", value: anomaly ? "Critical" : "Healthy" },
          ].map((card, index) => (
            <div
              key={index}
              style={{
                background: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
                boxShadow: "0 4px 12px rgba(0,0,0,0.4)",
              }}
            >
              <h3 style={{ marginBottom: "10px" }}>{card.label}</h3>
              <h2 style={{ fontSize: "22px", fontWeight: "bold" }}>
                {card.value}
              </h2>
            </div>
          ))}
        </div>

        {/* Charts */}
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px" }}>
          <div
            style={{
              background: "#1e293b",
              padding: "20px",
              borderRadius: "12px",
            }}
          >
            <h3>CPU and Memory Usage</h3>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={cpuMemoryData}>
                <CartesianGrid stroke="#334155" />
                <XAxis dataKey="time" stroke="#cbd5e1" />
                <YAxis stroke="#cbd5e1" />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="cpu_percent" stroke="#22c55e" />
                <Line type="monotone" dataKey="memory_percent" stroke="#3b82f6" />
              </LineChart>
            </ResponsiveContainer>
          </div>

          <div
            style={{
              background: "#1e293b",
              padding: "20px",
              borderRadius: "12px",
            }}
          >
            <h3>Disk I/O, NFS Latency, Error Rate</h3>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={diskNfsErrorData}>
                <CartesianGrid stroke="#334155" />
                <XAxis dataKey="time" stroke="#cbd5e1" />
                <YAxis stroke="#cbd5e1" />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="disk_io_mb_s" stroke="#f97316" />
                <Line type="monotone" dataKey="nfs_latency_ms" stroke="#ef4444" />
                <Line type="monotone" dataKey="error_rate_percent" stroke="#eab308" />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* AI Panel */}
  <div
  style={{
    marginTop: "40px",
    background: "#1e293b",
    padding: "20px",
    borderRadius: "12px",
  }}
>
  <h3 style={{ marginBottom: "15px" }}>AI Observability Agent</h3>

  <button
    onClick={handleAnalyze}
    style={{
      background: "#2563eb",
      padding: "10px 15px",
      borderRadius: "6px",
      border: "none",
      color: "white",
      cursor: "pointer",
      marginBottom: "15px",
    }}
  >
    Analyze Current Node
  </button>

  <button
    onClick={() => alert("ITSM Ticket Created (Simulated)")}
    style={{
      background: "#16a34a",
      padding: "10px 15px",
      borderRadius: "6px",
      border: "none",
      color: "white",
      cursor: "pointer",
      marginLeft: "10px",
      marginBottom: "15px",
    }}
  >
    Create ITSM Ticket
  </button>

  <div
    style={{
      marginTop: "15px",
      whiteSpace: "pre-wrap",
      lineHeight: "1.6",
      background: "#0f172a",
      padding: "15px",
      borderRadius: "8px",
      minHeight: "120px",
    }}
  >
    {analysis || "AI analysis will appear here."}
  </div>
</div>
      </div>
    </div>
  );
}

export default App;