# Results and Measurement Notes

## Wheel-speed controller comparison

The values in `controller_comparison.csv` summarize one recorded physical-controller comparison against a 0.1937 m/s velocity command.

| Controller | Mean speed (m/s) | MAE (m/s) | RMSE (m/s) |
|---|---:|---:|---:|
| Feedforward | 0.1606 | 0.0331 | 0.0502 |
| PID | 0.1558 | 0.0379 | 0.0380 |
| Feedforward + PID | 0.1916 | **0.0028** | **0.0036** |

These results are specific to the recorded robot, surface, calibration, and test conditions. They should be interpreted as project evidence rather than a universal controller benchmark.

## Checkpoint 2 evaluation

`particle_filter_timing.csv` and `slam_heading_tuning.csv` contain the measured values used to generate `slam_evaluation.png`.

### Mapping performance

- Divide-and-step ray tracing: 6.67 ms/scan
- Bresenham ray tracing: 4.04 ms/scan
- Evaluation length: 1,050 scans

### Localization accuracy

- Selected MCL configuration: 0.026 m position RMSE
- Odometry-only baseline: 0.149 m position RMSE
- Relative RMSE reduction: approximately 83%

### Particle-filter timing

| Particles | Average update time (ms) | Updates measured |
|---:|---:|---:|
| 100 | 18.26 | 600 |
| 300 | 48.82 | 600 |
| 500 | 78.28 | 600 |
| 1000 | 154.37 | 400 |

The linear timing fit projects a limit of about 641 particles within a 100 ms period. The selected 400-particle configuration takes approximately 64 ms per update.

### Real-robot SLAM tuning

| `k1` | Final correction (deg) | Peak correction (deg) | Result |
|---:|---:|---:|---|
| 0.015 | 11.2 | 15.3 | Two copies, rotated about 11 degrees |
| 0.005 | 12.2 | 15.7 | Two rotated copies |
| 0.001 | 8.6 | 10.2 | Two copies, smaller rotation |
| 0.0002 | 3.5 | 4.6 | One end doubled |
| 0.00001 | **1.1** | **1.5** | Single aligned maze |

## Reproducibility

Run the plotting scripts from the repository root:

```bash
python3 results/make_controller_chart.py
python3 results/make_slam_chart.py
```

The portfolio intentionally includes summarized measurements and plotting code, not course source code, submitted reports, or rosbag datasets.
