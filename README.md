# Student Engagement Intelligence and Retention Portfolio

**Author:** Ihor Melashchenko  
**Student ID:** C00290950  
**Module:** Data Science and Machine Learning 2  
**Institution:** South East Technological University  
**Date:** March 2026

## 📋 Overview

This portfolio extends my semester 1 work on student engagement and retention prediction in the context
of the **University App** (my final-year project). This version focuses on implementing and comparing additional
semester 2 techniques while maintaining the same problem domain and synthetic-data approach.

### Project Components

1. **Classical ML Foundations** - K-Means, KNN, and SVM on synthetic engagement and academic features
2. **Artificial Neural Networks** - ANN baseline for retention risk classification
3. **Deep Learning Preparation** - CNN/RNN/LSTM/Transformer-oriented notebook structure and environment checks
4. **Reinforcement Learning Intro** - Introductory environment and policy simulation workflow

## 🎯 Objectives

- Extend semester 1 engagement-retention analysis with semester 2 algorithm coverage
- Build consistent, reproducible notebook workflows with clear evaluation outputs
- Compare model behavior across clustering, classical classification, and neural approaches
- Document assumptions, limitations, and practical interpretation of results
- Produce portfolio evidence suitable for preliminary submission, final submission, and presentation

## 📊 Datasets

### Primary Data
- **Synthetic dataset** representing student engagement and academic behavior
- Features include app activity metrics (weekly logins, session duration, timetable views, notification interaction)
- Academic indicators include attendance, assignment submission rate, and GPA
- Binary retention-risk target included for supervised tasks

### Generated Files
- `data/processed/student_retention_dataset_v2.csv` - Generated and saved by Notebook 01
- Additional visual outputs saved under `results/figures/`

## 🛠️ Technologies & Tools

### Programming Language
- Python 3.x

### Development Environment
- Jupyter Notebook

### Core Libraries
- **Data Processing**: NumPy, Pandas
- **Visualization**: Matplotlib, Seaborn
- **Machine Learning**: Scikit-learn, XGBoost
- **Statistical Tools**: SciPy

### Version Control
- Git & GitHub

## 📁 Project Structure

```text
DS-and-ML-2-CA/
│
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── Data Science & Machine Learning 2 Continuous Assessment.pdf
│   └── work_log.md
│
├── notebooks/
│   ├── 01_classical_ml_foundations.ipynb
│   ├── 02_artificial_neural_networks.ipynb
│   ├── 03_deep_learning.ipynb
│   └── 04_reinforcement_learning_intro.ipynb
│
├── results/
│   └── figures/
│
└── src/
	└── data_generation.py
```

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.x installed.

### Running the Notebooks

1. Clone the repository:
```bash
git clone https://github.com/baldeagle0125/DS-and-ML-2-CA.git
cd DS-and-ML-2-CA
```

2. Create and activate a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Launch Jupyter Notebook:
```bash
jupyter notebook
```

5. Open and run notebooks in order:
   - `notebooks/01_classical_ml_foundations.ipynb`
   - `notebooks/02_artificial_neural_networks.ipynb`
   - `notebooks/03_deep_learning.ipynb`
   - `notebooks/04_reinforcement_learning_intro.ipynb`

### Execution Order

**Recommended sequence:**
1. Run Notebook 01 first (current most complete portfolio item)
2. Run Notebook 02 for ANN baseline
3. Run Notebook 03 for deep learning environment preparation and structure
4. Run Notebook 04 for reinforcement learning intro simulation

## 📈 Methodology

### Part 1: Classical ML Foundations

**Approach:** Unsupervised + Supervised Learning (K-Means, KNN, SVM)

1. Generate synthetic dataset from a reusable utility (`src/data_generation.py`)
2. Perform EDA and correlation analysis
3. Scale features and evaluate K-Means cluster quality (Elbow + Silhouette)
4. Visualize clusters using PCA
5. Train and tune KNN + SVM with GridSearchCV
6. Evaluate with Accuracy, ROC-AUC, classification reports, confusion matrices
7. Save visual evidence to `results/figures/`

### Part 2: Artificial Neural Networks

**Approach:** ANN baseline (current runnable version uses scikit-learn MLP)

1. Prepare train/test split and standardized features
2. Train MLP-based ANN baseline classifier
3. Evaluate with classification report

### Part 3: Deep Learning

**Approach:** Framework and environment validation for CNN/RNN/LSTM/Transformer sections

1. Notebook structure prepared for deep learning implementations
2. Environment check included to confirm TensorFlow availability

### Part 4: Reinforcement Learning Intro

**Approach:** Educational simulation workflow

1. Define simple retention-intervention environment
2. Run sample episode with action/reward transitions
3. Prepare notebook for next-stage policy-learning expansion

## 🔍 Key Findings (Preliminary)

- Notebook 01 executes end-to-end and produces reproducible visual and metric outputs
- K-Means produces identifiable engagement segments in PCA space
- Tuned SVM and KNN provide baseline retention-risk classification performance
- ANN baseline notebook is runnable and produces evaluation output

## 💡 Practical Applications

1. Early warning signals for student risk monitoring
2. Engagement segmentation for targeted intervention planning
3. Comparative model evidence to support data-informed support strategies
4. Foundation for scaling to richer deep-learning and RL experiments in final submission

## 📝 Documentation

The repository includes:

- `docs/work_log.md` for structured ongoing portfolio logging

## 🔗 Related Work

This portfolio directly extends my semester 1 portfolio and aligns with my University App project,
which includes student-facing services such as timetable access, notifications, and campus support features.

## 🎓 Academic Context

**Assessment Details:**
- Module: Data Science and Machine Learning 2
- Value: 60% of module grade
- Components:
  - Preliminary Submission (10%)
  - Final Portfolio Submission (80%)
  - In-class presentation (10%)

**Note:** This portfolio uses synthetic data for demonstration and reproducibility. Limitations and transferability
to real institutional data are discussed in notebook documentation.

**Last Updated:** March 29, 2026
