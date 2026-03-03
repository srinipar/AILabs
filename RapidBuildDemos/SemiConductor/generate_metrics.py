import pandas as pd
import numpy as np

np.random.seed(42)

timestamps = pd.date_range("2026-03-01 00:00", periods=150, freq="10T")

data = []

for ts in timestamps:
    for host in ["compute-node-01", "compute-node-02"]:
        
        # Normal baseline
        cpu = np.random.normal(55, 5)
        memory = np.random.normal(65, 4)
        disk_io = np.random.normal(120, 15)
        nfs_latency = np.random.normal(8, 2)
        error_rate = np.random.normal(0.5, 0.2)

        # Anomaly window
        if "02:00" <= ts.strftime("%H:%M") <= "03:00":
            cpu = np.random.normal(95, 2)
            memory = np.random.normal(85, 3)
            disk_io = np.random.normal(300, 20)
            nfs_latency = np.random.normal(150, 20)
            error_rate = np.random.normal(12, 2)

        data.append([
            ts,
            "eda-simulation-engine",
            host,
            round(cpu, 2),
            round(memory, 2),
            round(disk_io, 2),
            round(nfs_latency, 2),
            round(error_rate, 2)
        ])

df = pd.DataFrame(data, columns=[
    "timestamp",
    "service",
    "host",
    "cpu_percent",
    "memory_percent",
    "disk_io_mb_s",
    "nfs_latency_ms",
    "error_rate_percent"
])

df.to_csv("RapidBuildDemos/SemiConductor/metrics.csv", index=False)

print("metrics.csv generated successfully!")