import cv2

# Import the Haar Cascade classifier for face detection https://github.com/opencv/opencv/tree/master/data/haarcascades
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") 

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

# Open the video stream from the camera
video = cv2.VideoCapture(0)  # Change to 0 for webcam or use

def detect_faces(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return frame

while True:
    ret, frame = video.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    
    faces = detect_faces(frame)

    cv2.namedWindow("Face Detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Face Detection", 640, 480)
    cv2.imshow("Face Detection", faces)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()