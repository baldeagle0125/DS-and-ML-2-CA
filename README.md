# Student Engagement Intelligence and Retention Portfolio

**Author:** Ihor Melashchenko  
**Student ID:** C00290950  
**Module:** Data Science and Machine Learning 2  
**Institution:** South East Technological University  
**Date:** April 2026

## 📋 Overview

This portfolio extends semester 1 student engagement and retention analysis in the context of the **University App** (my final-year project). The semester 2 portfolio expands scope to cover each main machine learning topic from the module and presents a reproducible, evidence-based implementation.

### Project Components

1. **Classical ML Foundations** - K-Means, KNN, and SVM for engagement and retention-risk analysis
2. **Artificial Neural Networks** - MLP architecture comparison for retention-risk classification
3. **Deep Learning** - Sequence-based 1D CNN and LSTM comparative baseline
4. **Reinforcement Learning Intro** - Tabular Q-learning in a simplified intervention environment

## 🎯 Objectives

- Extend semester 1 retention analysis with full semester 2 algorithm coverage
- Implement all major module topics in runnable notebook workflows
- Benchmark synthetic and real-data behavior for transferability awareness
- Document practical model impact, limitations, and ethical boundaries
- Present work at a professional submission standard with reproducible outputs

## 📊 Datasets

### Primary Data

- **Synthetic student dataset** generated via `src/data_generation.py`
- Features include app behavior and academic engagement signals:
  - Weekly logins, average session duration, timetable views, notification click rate
  - Attendance rate, assignment submission rate, GPA
- Supervised target: synthetic `dropout_risk`

### Real Benchmark Data

- **UCI Student Performance** dataset (`data/raw/student-mat.csv`)
- Used as a benchmark comparison only (not institutional deployment data)
- Proxy target for comparison in Notebook 01: `dropout_risk_proxy = 1` when `G3 < 10`

### Generated Files

- `data/processed/student_retention_dataset_v2.csv`
- `data/processed/student_performance_real_processed.csv`

## 🛠️ Technologies & Tools

### Programming Language

- Python 3.x

### Development Environment

- Jupyter Notebook

### Core Libraries

- **Data Processing:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** scikit-learn, TensorFlow
- **Statistical Utilities:** SciPy

### Version Control

- Git and GitHub

### Why These Choices

- Python + Jupyter were chosen for transparent, notebook-first experimentation and presentation.
- scikit-learn provides reliable classical ML and ANN baselines with strong evaluation utilities.
- TensorFlow enables deep-learning implementation (CNN/LSTM) aligned with module outcomes.
- The hybrid synthetic + public benchmark strategy improves ethics, reproducibility, and comparative interpretation.

## 📁 Project Structure

```text
DS-and-ML-2-CA/
|
|-- README.md
|-- requirements.txt
|-- data/
|   |-- raw/
|   `-- processed/
|-- docs/
|   |-- Data Science & Machine Learning 2 Continuous Assessment.pdf
|   `-- work_log.md
|-- notebooks/
|   |-- 01_classical_ml_foundations.ipynb
|   |-- 02_artificial_neural_networks.ipynb
|   |-- 03_deep_learning.ipynb
|   `-- 04_reinforcement_learning_intro.ipynb
|-- results/
|   `-- figures/
`-- src/
     |-- __init__.py
     `-- data_generation.py
```

## 🚀 Getting Started

### Prerequisites

Ensure Python 3.x is installed.

### Running the Portfolio

1. Clone repository:

```bash
git clone https://github.com/baldeagle0125/DS-and-ML-2-CA.git
cd DS-and-ML-2-CA
```

2. Create and activate virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Launch Jupyter and run notebooks in order:

```bash
jupyter notebook
```

- `notebooks/01_classical_ml_foundations.ipynb`
- `notebooks/02_artificial_neural_networks.ipynb`
- `notebooks/03_deep_learning.ipynb`
- `notebooks/04_reinforcement_learning_intro.ipynb`

## 📈 Methodology

### Part 1: Classical ML Foundations

**Approach:** Unsupervised + Supervised Learning (K-Means, KNN, SVM)

1. Generate/load data and run EDA
2. Scale features and evaluate K-Means with elbow and silhouette
3. Visualize cluster structure with PCA
4. Tune KNN/SVM with `GridSearchCV`
5. Evaluate with accuracy, ROC-AUC, classification report, confusion matrix
6. Repeat tuned models on real benchmark data for synthetic-vs-real comparison

### Part 2: Artificial Neural Networks

**Approach:** ANN baseline and architecture comparison (`MLPClassifier`)

1. Standardized feature pipeline and train/test split
2. Architecture sweep: `(16,)`, `(32, 16)`, `(64, 32)`
3. Selection by test ROC-AUC and comparison diagnostics

### Part 3: Deep Learning

**Approach:** 1D CNN and LSTM sequence models

1. Build sequence-formatted input representation
2. Train/evaluate CNN and LSTM baselines
3. Compare F1 and ROC-AUC and save diagnostics visualization

### Part 4: Reinforcement Learning Intro

**Approach:** Tabular Q-learning

1. Define simplified retention intervention environment
2. Train epsilon-greedy Q-learning policy
3. Compare learned policy against random baseline

## 🔍 Key Findings

### Classical ML + Benchmark

- K-Means silhouette at `k=3`: `0.099`
- Synthetic KNN: accuracy `0.533`, ROC-AUC `0.440`
- Synthetic SVM: accuracy `0.617`, ROC-AUC `0.416`
- Real KNN: accuracy `0.570`, ROC-AUC `0.485`
- Real SVM: accuracy `0.709`, ROC-AUC `0.702`

### ANN

- Best ANN architecture: `(32, 16)`
- ROC-AUC: `0.562`
- Accuracy: `0.675`
- Minority-class F1: `0.05`

### Deep Learning

- LSTM: F1 `0.139535`, ROC-AUC `0.576250`
- 1D CNN: F1 `0.000000`, ROC-AUC `0.575313`

### Reinforcement Learning

- Random policy reward: `2.029`
- Learned policy reward: `4.700`

## 💡 Practical Applications

1. Early warning signals for student support teams
2. Engagement segmentation for targeted interventions
3. Comparative model evidence for retention analytics strategy
4. RL proof-of-concept for intervention policy framing

## 📝 Documentation

- `README.md`: full portfolio summary, methods, and outcomes
- `docs/work_log.md`: structured weekly log with outcomes, evidence, blockers, and next actions
- Notebook markdown + code comments: algorithm-level implementation reasoning and interpretation

## 🔗 Related Work

This portfolio directly extends my semester 1 portfolio and remains aligned with my University App project domain.

## 🎓 Academic Context

**Assessment Structure:**

- Preliminary Submission (10%)
- Final Portfolio Submission (80%)
- In-class Presentation (10%)

**Submission Readiness Status:**

- All required topic notebooks are implemented
- Core evidence artifacts are generated and present in `results/figures/`
- Structured development log is maintained
- Author/student identification is present across notebook and source files

## 📚 References

1. UCI Machine Learning Repository, Student Performance Data Set (Cortez and Silva, 2008).  
    URL: https://archive.ics.uci.edu/dataset/320/student+performance
2. scikit-learn documentation.  
    URL: https://scikit-learn.org/stable/
3. TensorFlow documentation.  
    URL: https://www.tensorflow.org/

**Last Updated:** April 21, 2026
