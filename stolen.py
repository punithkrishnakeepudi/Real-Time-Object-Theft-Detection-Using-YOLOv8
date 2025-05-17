import cv2
import os
import time
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # or your custom model

# Prepare folders
os.makedirs("trained_object/images", exist_ok=True)
os.makedirs("trained_object/labels", exist_ok=True)

# === Phase 1: TRAINING PHASE (Take ONE image of object) ===
cap = cv2.VideoCapture(0)
saved = False
print("[INFO] Training mode: Show the object to the camera...")

while not saved:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    names = model.names
    frame_h, frame_w = frame.shape[:2]

    # Remove humans from detection
    results.boxes = results.boxes[results.boxes.cls != 0]

    if len(results.boxes) > 0:
        print("[INFO] Object detected. Saving training image and label...")

        # Use the plot() to draw bounding boxes (YOLO-style)
        img_plotted = results.plot()
        cv2.imshow("Training Detection", img_plotted)

        # Save image
        train_img_path = "trained_object/images/trained.jpg"
        cv2.imwrite(train_img_path, frame)

        # Save label in YOLO format
        label_file = "trained_object/labels/trained.txt"
        with open(label_file, "w") as f:
            for box in results.boxes.data:
                x1, y1, x2, y2, conf, cls = box.tolist()

                x_center = ((x1 + x2) / 2) / frame_w
                y_center = ((y1 + y2) / 2) / frame_h
                width = (x2 - x1) / frame_w
                height = (y2 - y1) / frame_h

                f.write(f"{int(cls)} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

        saved = True
        print("[INFO] Training complete. Object and label saved.")
        time.sleep(2)

    else:
        cv2.imshow("Training Detection", frame)

    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cv2.destroyAllWindows()
cap.release()

# === Phase 2: MONITORING PHASE ===
print("[INFO] Monitoring started. Watching for theft...")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    names = model.names

    found_trained_object = False
    detected_human = False

    for box in results.boxes.data:
        x1, y1, x2, y2, conf, cls = box.tolist()
        class_id = int(cls)

        # Check if object is human
        if class_id == 0:
            detected_human = True
            continue

        # Mark object found
        found_trained_object = True

    plotted = results.plot()

    if not found_trained_object and detected_human:
        # Add alert text on frame
        cv2.putText(plotted, "🚨 Theft Detected: Object Missing", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

    cv2.imshow("Theft Detection", plotted)

      # Quit on ESC or Q
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        print("[INFO] Monitoring stopped by user.")
        break
cap.release()
cv2.destroyAllWindows()