import cv2
from ultralytics import YOLO


# model = YOLO("yolo11n.pt")
# model = YOLO("yolo11s.pt")
# model = YOLO("yolo11l.pt")
model = YOLO("yolo11m.pt")

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ Could not open webcam")
    exit()

print("✅ Webcam opened! Press Q to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Could not read frame")
        break
    results = model.track(frame, verbose=False, persist=True)
    annotated_frame = results[0].plot()
    
    cv2.imshow("Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


# models

# The fix is to use a slightly bigger model. YOLO comes in different sizes:
# ModelSizeSpeedAccuracy
# yolo11n.ptNano⚡ Fastest⭐ Basic
# yolo11s.ptSmall⚡ Fast⭐⭐ Better
# yolo11m.ptMedium🔄 Balanced⭐⭐⭐ Good
# yolo11l.ptLarge🐢 Slower⭐⭐⭐⭐ Great
# Since you have an NVIDIA GPU, you can afford a bigger model without losing much speed.
