import cv2
from ultralytics import solutions

cap = cv2.VideoCapture("/Users/glenn/gym_monitor/row/4920820-hd_1920_1080_25fps.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
model = "yolo11n-pose.pt"
gym = solutions.AIGym(
    model="yolo11n-pose.pt",
    show=True,
    kpts=[5, 11, 13],
    up_angle=100,
    down_angle=50, 
    line_width=4
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    im0 = gym.monitor(im0)
    # Assuming gym.monitor returns a dictionary or result object containing keypoints
    


cv2.destroyAllWindows()

