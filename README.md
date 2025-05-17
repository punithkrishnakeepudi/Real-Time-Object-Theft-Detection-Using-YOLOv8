# 🚨 Real-Time Object Theft Detection Using YOLOv8

This project implements a real-time theft detection system using the [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) model and OpenCV. It allows you to train the system on a custom object using your webcam and then continuously monitor its presence. If the object goes missing while a human is detected, it triggers an on-screen alert.

---

## 🎯 Use Case

This system is ideal for:
- Monitoring valuable items in low-security areas
- Detecting potential thefts in real-time
- Educational demos on computer vision and YOLO object detection
- DIY security camera projects

---

## 🧠 How It Works

### 1. **Training Phase**  
- Shows the object to your webcam
- YOLOv8 detects and stores the object image and label (excluding humans)

### 2. **Monitoring Phase**  
- Continuously checks for:
  - The presence of the trained object
  - The presence of a human
- If the object disappears **while a human is detected**, it displays a theft alert.

---

## 🚀 Installation

### 🧰 Requirements

- Python 3.8+
- OpenCV
- Ultralytics YOLOv8

### 🔧 Setup

```bash
# Clone this repository
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/punithkrishnakeepudi/Real-Time-Object-Theft-Detection-Using-YOLOv8.git)
cd Real-Time-Object-Theft-Detection-Using-YOLOv8

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
