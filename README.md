# 📸 Face Recognition Attendance System

A **real-time face recognition attendance system** built with **Python, OpenCV, and the `face_recognition` library**.  
The system detects and recognizes faces through a webcam and automatically marks attendance in a CSV file with timestamps.

---
<img width="1221" height="726" alt="Screenshot 2025-08-21 002849" src="https://github.com/user-attachments/assets/564b191e-68f3-4a17-a156-5e52e25cfeea" />




## 🚀 Features
- Detect and recognize faces using **HOG-based encodings** from the `face_recognition` library  
- **Real-time webcam feed** with bounding boxes around detected faces  
- Automatically mark **attendance in `Attendance.csv`** with name and time  
- Differentiates between **registered users** (green box) and **unregistered users (NPC)** (red box)  
- Simple, efficient, and easy to extend  

---

## 🛠️ Tech Stack
- **Python**  
- **OpenCV** – for real-time video processing  
- **face_recognition** – for facial encoding and comparison  
- **NumPy** – for numerical operations  
- **CSV** – for storing attendance logs  

---

## 📂 How It Works
1. Store images of people in the `people/` folder (filenames = person’s name).  
2. Encodings of known faces are generated and stored in memory.  
3. The webcam feed is processed frame by frame:
   - Faces are detected and encoded  
   - Matches are checked against the stored encodings  
   - Attendance is marked with **Name + Timestamp** in `Attendance.csv`  

---

## ▶️ Usage

Install dependencies:

```bash
pip install opencv-python face_recognition numpy
