# Object_Surface_Detection_with_CNN


# 📄 README.md

```markdown
# NEU Surface Defect Detection using CNN

This project implements a **Convolutional Neural Network (CNN)** to detect surface defects in steel products using the **NEU Surface Defect Dataset**. It also includes a **Streamlit web application** to upload images and get real-time predictions.

---

## 🏆 Project Highlights

- **Model:** Custom CNN with 3 convolutional layers + fully connected layers.  
- **Dataset:** NEU Surface Defect Dataset (6 defect types).  
- **Accuracy:** Training Accuracy: 91% | Validation Accuracy: 91%  
- **Deployment:** Streamlit app for real-time defect detection.  

---

## 📂 Dataset Structure

```

NEU-DET/
├── train/
│   ├── crazing/
│   ├── inclusion/
│   ├── patches/
│   ├── pitted_surface/
│   ├── rolled-in-scale/
│   └── scratches/
├── validation/
│   ├── crazing/
│   ├── inclusion/
│   ├── patches/
│   ├── pitted_surface/
│   ├── rolled-in-scale/
│   └── scratches/

```

> Each subfolder contains images of the corresponding defect type.

**Dataset Source:** [NEU Surface Defect Dataset on Kaggle](https://www.kaggle.com/datasets/andrewmvd/steel-defect-detection)

---

## 🛠️ Project Structure

```

SmartDefectDetection/
│
├─ NEU-DET/                  # Dataset folder
├─ models/                    # Saved CNN model
│   └─ baseline_cnn_net.h5
├─ scripts/
│   ├─ train_baseline.py      # Train CNN model
│   ├─ evaluate.py            # Evaluate model performance
│   └─ app.py                 # Streamlit application
├─ requirements.txt
└─ README.md

````

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/PrathamBaraskar/Object_Surface_Detection_with_CNN
cd SmartDefectDetection
````

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

## 🏋️‍♂️ Training the CNN Model

Run the training script to train the CNN model:

```bash
python scripts/train_baseline.py
```

* The trained model will be saved in the `models/` folder as `baseline_cnn_net.h5`.
* Training and validation accuracy ~ **91%**.

---

## 📊 Evaluating the Model

Evaluate the trained model using:

```bash
python scripts/evaluate.py
```

* Generates **classification report** and **confusion matrix**.
* Helps visualize model performance on validation data.

---

## 🌐 Streamlit Web Application

You can test the model on new images using the Streamlit app.

1. Navigate to the `scripts/` folder:

```bash
cd scripts
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Upload any defect image and view the **predicted defect type** in real-time.

---

## 📝 CNN Architecture

| Layer Type      | Output Shape | Notes           |
| --------------- | ------------ | --------------- |
| Conv2D + ReLU   | 128x128x32   | Kernel 3x3      |
| MaxPooling2D    | 64x64x32     | Pool size 2x2   |
| Conv2D + ReLU   | 64x64x64     | Kernel 3x3      |
| MaxPooling2D    | 32x32x64     | Pool size 2x2   |
| Conv2D + ReLU   | 32x32x128    | Kernel 3x3      |
| MaxPooling2D    | 16x16x128    | Pool size 2x2   |
| Flatten         | 32768        |                 |
| Dense + ReLU    | 128          | Fully connected |
| Dropout         | 128          | Rate 0.5        |
| Dense + Softmax | 6            | Output classes  |

---

## ✅ Key Features

* Detects **6 types of steel surface defects**:
  `crazing, inclusion, patches, pitted_surface, rolled-in-scale, scratches`
* **High accuracy CNN model** for industrial automation tasks.
* **Streamlit app** for real-time testing of new images.
* Easy to extend with **transfer learning** or **Grad-CAM visualization** in future.

---

## 📈 Results

* Training Accuracy: **91%**
* Validation Accuracy: **91%**
* Confusion matrix and classification report available in `evaluate.py`.

---

## 📌 Future Enhancements

* Integrate **Grad-CAM** to visualize defect areas.
* Use **transfer learning** (ResNet, EfficientNet) to improve accuracy.
* Deploy on a **web server or cloud** for industry-level use.

---

## 📚 References

* NEU Surface Defect Dataset: [Kaggle]([https://www.kaggle.com/datasets/andrewmvd/steel-defect-detection](https://www.kaggle.com/datasets/kaustubhdikshit/neu-surface-defect-database))
* Keras CNN Tutorial: [https://keras.io/examples/vision/cnn/](https://keras.io/examples/vision/cnn/)
* Streamlit Documentation: [https://docs.streamlit.io/](https://docs.streamlit.io/)

```

---

This README:  

- Explains **dataset, model, training, evaluation, and deployment**.  
- Shows **accuracy** and CNN architecture.  
- Is **professional and GitHub-ready**.  

---

If you want, I can also **create a version with screenshots of the Streamlit app and predicted results** to make it **even more visually appealing on GitHub**.  

Do you want me to do that next?
```
