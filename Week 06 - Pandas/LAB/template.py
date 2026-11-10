"""
RECORD CHECK  -  my version
===========================

Name  : Hetansh Patel
Lane  :  AI  
Date  : 08/11/2026

Run it:   python template.py


"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Week 06 - Pandas/LAB/own.csv")

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

df["status"] = df["percent"].apply(
    lambda percent: "OVER LIMIT" if percent >= 100
    else "WARNING" if percent >= 90
    else "OK"
)

print("Full results:")
print(df)

print("\nServers that need attention:")
print(df[df["status"] != "OK"])

status_counts = df.groupby("status").size()

print("\nCount per status:")
print(status_counts)

df.to_csv("storage_results.csv", index=False)

status_counts.plot(
    kind="bar",
    title="Servers per Status",
    xlabel="Status",
    ylabel="Number of Servers",
    rot=0
)

plt.tight_layout()
plt.savefig("status_counts.png")
plt.close()
