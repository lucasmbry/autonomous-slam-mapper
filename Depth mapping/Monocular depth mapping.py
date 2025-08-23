import cv2

"""
# Open the video stream from the RTSP URL
# RPi cmd: libcamera-vid -t 0 -n --low-latency --framerate 20 --profile high --intra 10 --codec libav --libav-format mpegts -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream1}'
video = cv2.VideoCapture("rtsp://192.168.0.145:8554/stream1")
if not video.isOpened():
    raise Exception("Could not open video device")
"""

"""
# Open the video stream from GStreamer pipeline
# rpicam-vid -t 0 -n --codec libav --libav-format mpegts -o - | gst-launch-1.0 fdsrc fd=0 ! udpsink host=<ip-addr> port=<port>
gst_str = (
    "udpsrc port=8554 ! "
    "tsdemux ! h264parse ! avdec_h264 ! videoconvert ! appsink"
)
video = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
"""

# Open the video stream from webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Camera", 640, 480)
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()