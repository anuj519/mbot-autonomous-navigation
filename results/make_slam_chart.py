"""Generate recruiter-facing Checkpoint 2 evaluation charts."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


HERE = Path(__file__).resolve().parent
TIMING = pd.read_csv(HERE / "particle_filter_timing.csv")
TUNING = pd.read_csv(HERE / "slam_heading_tuning.csv")

plt.style.use("seaborn-v0_8-whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), constrained_layout=True)

# Particle-filter scaling on the Raspberry Pi.
x = TIMING["particles"].to_numpy()
y = TIMING["average_update_time_ms"].to_numpy()
slope, intercept = np.polyfit(x, y, 1)
fit_x = np.linspace(0, 1050, 200)
limit_particles = (100.0 - intercept) / slope

axes[0].scatter(x, y, color="#1f6f8b", s=65, zorder=3, label="Measured")
axes[0].plot(fit_x, slope * fit_x + intercept, color="#58a6c7", linewidth=2, label="Linear fit")
axes[0].axhline(100, color="#bf4b4b", linestyle="--", linewidth=1.8, label="10 Hz budget")
axes[0].axvline(limit_particles, color="#6a5acd", linestyle=":", linewidth=1.8)
axes[0].annotate(
    f"Projected limit: {limit_particles:.0f} particles",
    xy=(limit_particles, 100),
    xytext=(420, 135),
    arrowprops={"arrowstyle": "->", "color": "#444444"},
    fontsize=10,
)
axes[0].set_title("Particle-filter runtime on Raspberry Pi")
axes[0].set_xlabel("Particles")
axes[0].set_ylabel("Mean update time (ms)")
axes[0].set_xlim(0, 1050)
axes[0].set_ylim(0, 170)
axes[0].legend(frameon=False, loc="upper left")

# Real-bag action-model tuning.
labels = ["0.015", "0.005", "0.001", "0.0002", "0.00001"]
bars = axes[1].bar(labels, TUNING["final_correction_deg"], color=["#9b5d5d"] * 4 + ["#2a9d8f"])
axes[1].set_title("SLAM heading correction after tuning")
axes[1].set_xlabel("Rotational-noise coefficient k1")
axes[1].set_ylabel("Final map-to-odom correction (deg)")
axes[1].bar_label(bars, fmt="%.1f°", padding=3, fontsize=9)
axes[1].annotate(
    "Single aligned map",
    xy=(4, 1.1),
    xytext=(2.7, 6.0),
    arrowprops={"arrowstyle": "->", "color": "#444444"},
    fontsize=10,
)
axes[1].set_ylim(0, 14)

fig.suptitle("Physical MBot SLAM evaluation", fontsize=16)
fig.savefig(HERE / "slam_evaluation.png", dpi=220, bbox_inches="tight")
