# BlinkType Assist 👁️💬

**BlinkType Assist** is an innovative assistive typing application that allows users to interact with a virtual keyboard using only **eye gaze direction** and **blinking gestures**.

This project is specially designed for individuals with **motor impairments or limited mobility**, enabling hands-free digital communication and interaction.

---

## 💡 Features

- 👀 Eye gaze-controlled keyboard navigation  
- 👁️ Blink-based text input  
- 🎯 Real-time facial landmark detection using `dlib` and `OpenCV`  
- 🧠 Intuitive UI for accessible interaction  
- 🧩 Customizable key layout

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** OpenCV, dlib, imutils  
- **Face Detection:** Facial Landmark Predictor (68-point model)  
- **Platform:** Desktop Application

---

## 🚀 How to Run

### 1. Clone the repository


git clone https://github.com/hanifjamadar77/BlinkType-Assist.git
cd BlinkType-Assist

---

## ⚙️ Setting Up dlib Environment (Windows)

Installing `dlib` can be tricky on Windows. Follow these steps to ensure a smooth setup:

### 🔧 1. Install CMake and Visual Studio Build Tools

- Install **[CMake](https://cmake.org/download/)**  
- Install **[Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)** with:
  - C++ build tools
  - Windows 10 SDK

> ⚠️ These are needed to build `dlib` from source.

---

### 🐍 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```
# Outputs:
![image](https://github.com/user-attachments/assets/072910fb-5244-4a12-9429-a1da38e2cd69)

