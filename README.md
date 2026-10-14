# Autonomous Monocular SLAM Depth Mapper

Real-time spatial mapping and 3D scene reconstruction pipeline using monocular depth estimation (MDE), low-latency video streaming from a robotic car

* **Objective:** 3D point cloud generation and spatial mapping from a single monocular camera feed
* **Architecture:** Video streaming via an RC platform offloaded to my laptop running neural depth estimation and ROS slam node

* **Monocular Depth Estimation:** Uses Depth Anything V2 to infer dense metric depth maps from single-frame RGB feeds
* **Low-Latency Streaming:** Hardware-accelerated GStreamer pipeline streaming camera frames from vehicle to host
* **Point Cloud Generation:** Converts RGB-D data into dense 3D point clouds in real time.
* **Ground Plane Segmentation:** Planar estimation algorithms to detect and isolate the ground reference plane
* **Odometry & Sensor Fusion:** Wheel encoder feedback integrated into ROS for odometry tracking and drift reduction
