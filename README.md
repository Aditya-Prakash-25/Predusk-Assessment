# Mini Project: ML Classification and Generative AI

This repository contains a small-scale project demonstrating the use of a neural network for classification and a pre-trained generative model for text generation using Hugging Face Transformers.

---

## 📁 Contents

- `into_to_generative_ai.py`: Python script for generating text using GPT-2.
- `generated_outputs.txt`: File storing generated outputs from GPT-2 with different temperature settings.
- `Figure.png`: Line plot showing training and testing accuracy vs epoch.
- `mini_report.tex`: LaTeX report combining insights from the classification and generation tasks.
- `README.md`: This documentation file.

---

## 🔧 1. ML Classification Task

### Dataset
- **Dataset Used**: Iris Dataset (150 samples, 3 classes, 4 features)

### Model
- A simple 2-layer fully connected neural network using PyTorch.
- Hidden layer: 16 ReLU units  
- Output: 3 classes (softmax via `CrossEntropyLoss`)  
- Optimizer: SGD  
- Learning Rate: 0.01  
- Epochs: 50  
- Batch size: 150 (full batch)

### Output
- Final Training Accuracy: ~31%  
- Final Test Accuracy: ~33%  
- Accuracy vs Epoch plot saved as `Figure.png`.

---

## ✨ 2. Generative AI Task

### Tool
- Hugging Face `transformers` library  
- Model: Pretrained `gpt2`

### Prompt
```
Once upon a time
```

### Output Temperatures
- **Temperature 0.7**: More coherent and repetitive output  
- **Temperature 1.0**: More creative, diverse, but less structured output

Output is saved in `generated_outputs.txt`.

---

## 📝 3. LaTeX Report

The file `mini_report.tex` contains:
- Classification model summary and accuracy plot  
- GenAI output samples and comparison  
- Key learnings from both tasks

### How to Compile
```bash
pdflatex mini_report.tex
```

Or compile using [Overleaf](https://overleaf.com).

> ⚠️ Make sure `Figure.png` is in the same folder while compiling.

---

## ✅ Requirements

Install the following Python packages before running:
```bash
pip install torch transformers matplotlib
```

---

## 🙋 Author

**Aditya Prakash**

This project was created as part of an introductory module on Machine Learning and Generative AI.
