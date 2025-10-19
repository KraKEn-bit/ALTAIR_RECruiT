# 🐦 Bird Species Detection using YOLOv11

This project focuses on building a **deep learning–based bird species detection system** using the **YOLOv11 object detection model**.  
The goal is to train a model capable of accurately identifying different bird species — **Sparrow, Owl, and Eagle** — from images.

---

## 📘 Project Overview

The system was trained on a **custom annotated dataset** prepared in **Roboflow** and trained in **Google Colab** using **GPU acceleration** for faster performance.  
It leverages **Ultralytics YOLOv11 (nano)** for efficient and accurate object detection.

---

## ⚙️ Model Details

| Attribute | Description |
|------------|--------------|
| **Model Type** | YOLOv11 (Nano) |
| **Framework** | Ultralytics YOLO |
| **Training Environment** | Google Colab (T4 GPU enabled) |
| **Dataset Source** | Roboflow (Custom annotated dataset) |
| **Training Epochs** | 50 |
| **Loss Function** | YOLO Object Detection Loss |
| **Optimizer** | SGD / Adam (Default YOLO settings) |

---

## 📊 Model Performance

| Metric | Value |
|---------|--------|
| **mAP@50** | 89.3% |
| **Precision** | 96.3% |
| **Recall** | 83.9% |

---

## 🧩 Project Workflow

### 1️⃣ Dataset Preparation  
- Collected images of various bird species (**Sparrow**, **Owl**, **Eagle**).  
- Annotated images using **Roboflow’s bounding box annotation tool** for object detection.  
- Exported the dataset in **YOLOv11 PyTorch format**.

### 2️⃣ Model Training  
- Loaded the **YOLOv11 model** using **Ultralytics** in **Google Colab**.  
- Imported the Roboflow dataset via API.  
- Trained the model for **50 epochs** using GPU for faster convergence.

### 3️⃣ Model Evaluation  
- Evaluated the model using the **test split** of the dataset.  
- Computed key performance metrics: **mAP@50**, **Precision**, and **Recall**.

### 4️⃣ Prediction & Visualization  
- Tested the model on **unseen bird images**.  
- Visualized predictions with **bounding boxes and species labels**.  
- Initially, some annotations didn’t display correctly, so the dataset was **restructured and retrained** for improved results.  
- The final model successfully generated accurate detection outputs with proper annotations.

---

## 🧠 Technologies Used

- **Python**  
- **YOLOv11 (Ultralytics)**  
- **Google Colab**  
- **Roboflow**  
- **PyTorch**

---

