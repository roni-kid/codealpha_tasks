# 👁️ CodeAlpha — Object Detection & Tracking

A real-time object detection and tracking system using YOLOv11 and OpenCV. Detects 80 different object types from a webcam feed and assigns unique tracking IDs to each object.

---

## 📸 Preview

> Real-time webcam feed with bounding boxes, labels, confidence scores and tracking IDs drawn on detected objects.

---

## ✨ Features

- 🎯 Real-time **object detection** using YOLOv11
- 🔢 **Object tracking** with unique IDs per object
- 📷 Works with **webcam** or video files
- ⚡ Detects **80 object types** — people, cars, phones, bottles and more
- 🖥️ Live display with bounding boxes and confidence scores
- ❌ Press **Q** to quit cleanly

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| OpenCV | Webcam input and display |
| Ultralytics YOLO | Object detection model |
| PyTorch | Deep learning backend |

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_ObjectDetection.git
cd CodeAlpha_ObjectDetection
```

**2. Create a virtual environment**
```bash
python -m venv env
env\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
python detector.py
```

> On first run, YOLOv11s model (~20MB) will auto-download.
> Press **Q** to quit the detection window.

---

## ⚙️ Configuration

Inside `detector.py` you can change:

```python
# Change camera (0, 1, 2...)
cap = cv2.VideoCapture(1)

# Change YOLO model size
model = YOLO("yolo11s.pt")   # nano=fastest, small=balanced, medium=accurate
```

---

## 📁 Project Structure

```
CodeAlpha_ObjectDetection/
├── detector.py       ← Main application file
├── yolo11s.pt        ← YOLO model (auto-downloaded)
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

```
opencv-python
ultralytics
```

---

## 🧠 How It Works

1. **Video capture** — OpenCV opens the webcam and reads frames
2. **Detection** — Each frame is passed to YOLOv11 which detects objects and draws bounding boxes
3. **Tracking** — `.track()` assigns persistent IDs to objects across frames
4. **Display** — Annotated frames are shown in real time

---

## 👨‍💻 Author

Built as part of the **CodeAlpha AI Internship Program**

> Connect with me on LinkedIn: [Your LinkedIn]
> GitHub: [Your GitHub]
