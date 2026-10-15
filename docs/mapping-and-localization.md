# Mapping and Localization

## Current status

Checkpoint 2 is in progress. The physical mapping pipeline has produced a saved occupancy grid named `realmap1` with the following properties:

- **Grid size:** 200 x 200 cells
- **Resolution:** 0.05 m/cell
- **Mapped area:** 10 m x 10 m
- **Primary sensors:** wheel encoders and 2D LiDAR

## Mapping pipeline

The team-integrated mapping pipeline follows these stages:

1. Associate each LiDAR beam with an interpolated robot pose to reduce motion distortion across a scan.
2. Trace each beam through the grid to identify traversed free-space cells.
3. Mark the measured endpoint as occupied.
4. Accumulate evidence through bounded log-odds updates.
5. Publish and inspect the occupancy grid in RViz or Foxglove.

My completed work so far includes bringing up the physical pipeline, collecting a real-world map, saving the resulting map artifacts, and inspecting the output resolution and coverage. Mapping implementation within the team repository includes contributions from other team members.

## Monte Carlo localization

The current individual development focus is the particle-filter localization stage:

- Drawing and resampling particles
- Propagating pose hypotheses with a probabilistic action model
- Scoring hypotheses using LiDAR endpoint likelihoods
- Normalizing particle weights
- Computing a weighted position and circular mean heading
- Comparing the estimated trajectory with a reference path

These items are described as work in progress until the implementation and validation run are complete.

## Next evidence to add

- Final occupancy-map image
- Particle-cloud visualization
- Estimated-versus-reference trajectory plot
- Localization or SLAM run video
- Quantitative or repeatable evaluation results

