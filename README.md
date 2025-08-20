# 📸 Face Recognition Attendance System

A **real-time face recognition attendance system** built with **Python, OpenCV, and the `face_recognition` library**.  
The system detects and recognizes faces through a webcam and automatically marks attendance in a CSV file with timestamps.

---

<img width="967" height="766" alt="Screenshot 2025-08-20 231326" src="https://github.com/user-attachments/assets/e8e748b3-fe5c-4d32-8fef-6123a9d71d31" />

<img width="987" height="833" alt="Screenshot 2025-08-20 231245" src="https://github.com/user-attachments/assets/cbb1688d-eca7-4c9b-a343-a2aa809eefac" />

<img width="453" height="132" alt="Screenshot 2025-08-20 231354" src="https://github.com/user-attachments/assets/1c5c1eec-d614-4718-a4d4-d92b24088be8" />


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
