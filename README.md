# PalmPlay
"Real-time hand gesture control system for racing games using MediaPipe and OpenCV."
# 🖐️ Gesture-Controlled Car Game using MediaPipe & OpenCV

This project allows you to **control a car in PC games** using your **hand gestures in real-time**, leveraging the power of **MediaPipe**, **OpenCV**, and **Python**.

No game controller.  
No keyboard.  
Just your hands.

---

## 🎮 Features

- ✋ **Open both hands** → Accelerate (W)
- ✊ **Close both hands** → Brake (S)
- 👈 **Left hand open, right closed** → Turn Left (WA)
- 👉 **Right hand open, left closed** → Turn Right (WD)
- 👻 **Hands off camera** → Stops all movement (safety mechanism)

All this happens **live**, with camera input and simulated `W`, `A`, `S`, `D` keystrokes via Python.

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| [Python 3.10+](https://www.python.org/downloads/release/python-3100/) | Primary programming language |
| [MediaPipe](https://google.github.io/mediapipe/) | Real-time hand detection and gesture tracking |
| [OpenCV](https://opencv.org/) | Webcam input + image processing |
| [pynput](https://pynput.readthedocs.io/en/latest/) | Simulates keypresses (`W`, `A`, `S`, `D`) for game control |

---

## 📦 Installation

### 1. Clone this repo
```bash
git clone https://github.com/CoderAmbar/PalmPlay.git
cd gesture-control-car
