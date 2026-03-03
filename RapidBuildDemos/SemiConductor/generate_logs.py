logs = []

for i in range(10):
    logs.append([
        "2026-03-01 02:1" + str(i),
        "eda-simulation-engine",
        "compute-node-01",
        "ERROR",
        "License checkout timeout from license-server-01"
    ])
    
    logs.append([
        "2026-03-01 02:2" + str(i),
        "eda-simulation-engine",
        "compute-node-02",
        "ERROR",
        "NFS storage latency threshold exceeded"
    ])

import pandas as pd

df_logs = pd.DataFrame(logs, columns=[
    "timestamp",
    "service",
    "host",
    "level",
    "message"
])

df_logs.to_csv("RapidBuildDemos/SemiConductor/logs.csv", index=False)

print("logs.csv generated successfully!")