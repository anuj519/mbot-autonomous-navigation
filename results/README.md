# Results and Measurement Notes

## Wheel-speed controller comparison

The values in `controller_comparison.csv` summarize one recorded physical-controller comparison against a 0.1937 m/s velocity command.

| Controller | Mean speed (m/s) | MAE (m/s) | RMSE (m/s) |
|---|---:|---:|---:|
| Feedforward | 0.1606 | 0.0331 | 0.0502 |
| PID | 0.1558 | 0.0379 | 0.0380 |
| Feedforward + PID | 0.1916 | 0.0028 | 0.0036 |

These results are specific to the recorded robot, surface, calibration, and test conditions. They should be interpreted as project evidence rather than a universal controller benchmark.

## Physical square run

The final repeated-square rosbag lasted approximately 144 seconds and recorded odometry and velocity-command data throughout the run. The demonstration completed four consecutive square trajectories and ended close to its starting region.

The final trajectory plot will be added when the original rosbag-derived image is exported from the robot workspace.

## Mapping

The current saved occupancy map contains 200 x 200 cells at 0.05 m/cell. The map image will be added after the Checkpoint 2 result is finalized.

