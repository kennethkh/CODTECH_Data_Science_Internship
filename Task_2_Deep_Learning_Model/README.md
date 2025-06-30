# Task 2: Deep Learning Model for Image Classification

This task involves building a deep learning model using **TensorFlow/Keras** to classify handwritten digits from the **MNIST** dataset.

The model is a simple feedforward neural network trained and evaluated using the built-in MNIST data provided by TensorFlow.

---

## 📁 File Included

- `task2_image_classification_colab.ipynb`: A Google Colab-ready notebook containing:
  - Data loading and normalization
  - Model creation using Keras Sequential API
  - Training and validation
  - Evaluation and visualization

---

## 🧠 Model Architecture

- `Flatten` input layer (28x28 → 784)
- `Dense(128, activation='relu')`
- `Dense(10, activation='softmax')`

---

## 🚀 How to Run

1. Open the notebook in [Google Colab](https://colab.research.google.com).
2. Enable GPU via `Runtime > Change runtime type > GPU` (optional but recommended).
3. Run each cell sequentially.

---

## 📊 Output

- Final test accuracy printed after evaluation.
- Accuracy and validation graphs plotted over epochs.

---

## 🛠️ Libraries Used

- TensorFlow
- Matplotlib

---

## ✅ Result

The trained model achieves high accuracy on the MNIST dataset and demonstrates the ability to classify digits with minimal error.
