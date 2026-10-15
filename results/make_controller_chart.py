"""Generate the controller-comparison figure from the portfolio CSV."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


HERE = Path(__file__).resolve().parent
DATA = pd.read_csv(HERE / "controller_comparison.csv")

labels = DATA["controller"].tolist()
colors = ["#8da9c4", "#627d98", "#1f7a8c"]

plt.style.use("seaborn-v0_8-whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), constrained_layout=True)

speed_bars = axes[0].bar(labels, DATA["mean_measured_speed_mps"], color=colors)
axes[0].axhline(
    DATA["command_speed_mps"].iloc[0],
    color="#b23a48",
    linestyle="--",
    linewidth=2,
    label="Command: 0.1937 m/s",
)
axes[0].set_title("Mean wheel-speed tracking")
axes[0].set_ylabel("Speed (m/s)")
axes[0].set_ylim(0, 0.22)
axes[0].legend(frameon=False, loc="lower right")
axes[0].tick_params(axis="x", rotation=12)
axes[0].bar_label(speed_bars, fmt="%.4f", padding=3, fontsize=9)

x = range(len(labels))
width = 0.36
mae_bars = axes[1].bar(
    [value - width / 2 for value in x],
    DATA["mae_mps"],
    width,
    label="MAE",
    color="#1f7a8c",
)
rmse_bars = axes[1].bar(
    [value + width / 2 for value in x],
    DATA["rmse_mps"],
    width,
    label="RMSE",
    color="#bf7b54",
)
axes[1].set_title("Tracking-error comparison")
axes[1].set_ylabel("Error (m/s)")
axes[1].set_xticks(list(x), labels, rotation=12)
axes[1].legend(frameon=False)
axes[1].bar_label(mae_bars, fmt="%.4f", padding=3, fontsize=9)
axes[1].bar_label(rmse_bars, fmt="%.4f", padding=3, fontsize=9)

fig.suptitle("Physical MBot wheel-speed controller comparison", fontsize=15)
fig.savefig(HERE / "controller_comparison.png", dpi=220, bbox_inches="tight")

