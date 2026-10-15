# Controls and Odometry

## Objective

The controls milestone converted high-level velocity and waypoint commands into repeatable physical motion. The main engineering problem was that identical PWM commands do not produce identical wheel speeds: motor variation, surface friction, battery state, encoder quantization, and drivetrain geometry all affect the response.

## Controller evaluation

Three wheel-speed control configurations were evaluated on the physical robot:

1. **Feedforward:** predicts the motor command from an experimentally calibrated speed-to-PWM relationship.
2. **PID feedback:** corrects wheel-speed error from encoder measurements.
3. **Feedforward + PID:** supplies the nominal calibrated command and uses feedback to correct the remaining error.

For the recorded comparison, the combined controller tracked a 0.1937 m/s command with a mean measured speed of 0.1916 m/s, 0.0028 m/s MAE, and 0.0036 m/s RMSE. It substantially outperformed the standalone feedforward and PID configurations in that run.

## Waypoint motion control

The C++ motion controller follows a rotate-translate-rotate sequence:

1. Rotate toward the waypoint.
2. Drive toward the target position.
3. Rotate to the requested final heading.

The controller was tested through repeated physical square trajectories. Odometry could report a path that appeared geometrically consistent while the real robot accumulated systematic heading error, so physical endpoint behavior—not odometry alone—was used during calibration.

## Lessons from physical testing

- A controller that looks correct in logged odometry can still be wrong in the room.
- Feedforward calibration handles most of the nominal motor effort; feedback is then responsible for smaller corrections.
- Small errors in effective wheelbase or differential-drive geometry accumulate over repeated turns.
- Surface changes alter traction and can invalidate a calibration collected elsewhere.
- Rosbag recordings make it possible to compare controller behavior without relying only on visual judgment.

