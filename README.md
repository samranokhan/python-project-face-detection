
# 🧠 Python Project: Real-Time Face Detection using OpenCV

This project is a simple and effective **real-time face detection system** built using Python and OpenCV. It captures video from your system's webcam and detects human faces using the Haar Cascade Classifier.

---

## 📸 Features

- Real-time face detection from webcam feed
- Uses Haar Cascade Classifier (`haarcascade_frontalface_default.xml`)
- Draws green bounding boxes around detected faces
- Press `'a'` key to stop the video feed

---

## 🛠 Requirements

Make sure you have the following installed:

- Python 3.x
- OpenCV (`cv2`)

Install OpenCV using pip if you haven’t already:
```bash
pip install opencv-python
```

---

## 🚀 How to Run

1. **Download Haar Cascade File**  
   Get `haarcascade_frontalface_default.xml` from the [OpenCV GitHub repo](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and place it in your project directory.

2. **Run the Python Script**
```bash
python face_id.py
```

3. **Instructions**
   - A new window will open showing your webcam feed.
   - Detected faces will be highlighted in green rectangles.
   - Press the **'a'** key to close the camera and exit the program.

---

## 🧾 File Structure

```
📂 python-project-face-detection
 ┣ 📄 face_id.py                   # Main face detection script
 ┣ 📄 README.md                    # Project overview and instructions
 ┣ 📄 LICENSE                      # MIT License
 ┗ 📄 haarcascade_frontalface_default.xml   # Face detection model
```

---

## 📝 Notes

- Make sure your webcam is connected and working.
- The index `cv2.VideoCapture(1)` may need to be changed to `0` if the default camera is not recognized.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 🙋‍♂️ Author

**Samran Khan**  
For any queries, feel free to connect via [GitHub](https://github.com/samranokhan)
