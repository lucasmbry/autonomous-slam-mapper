# Autonomous monocular SLAM mapper
As part of a recent interest in computer vision and 3D scene recreation I am working on implementing an MDE model onto a remotely controlled vehicle to map spaces with ROS.

## Current progress

![](https://geps.dev/progress/30)

 - [x] Implement MDE model. (Currently DepthAnythingV2)
 - [ ] Real time implementation on host.
     - [ ] Parse depth cloud to ROS.
 - [x] Develop simple remotely controlled car.
 - [x] Send live camera footage to host computer.
     - [ ] Reduce camera latency using GStreamer
 - [ ] Positional feedback via encoders to ROS.
 - [ ] TBD...