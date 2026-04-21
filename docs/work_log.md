# Portfolio Work Log

**Author:** Ihor Melashchenko  
**Student ID:** C00290950  
**Module:** Data Science and Machine Learning 2

## 📋 Purpose

This document tracks practical progress for the semester 2 portfolio.

## 🧭 Logging Method

1. Each entry records work done, practical impact, and next steps.
2. Weekly logging is used for consistent portfolio tracking through the semester.

## 📝 Entry Template

- Date:
- Task:
- Changes made:
- Practical impact:
- Reflection/next action:

## 📅 Weekly Log (From Week of January 19, 2026)

### Week of 2026-01-19

- Task:
  - Set up repository structure for DS&ML 2 portfolio, extending semester 1 theme on student engagement and retention.
- Changes made:
  - Created folders: data/, docs/, notebooks/, results/, src/.
  - Initialized README.md with project overview and objectives.
  - Added requirements.txt with core dependencies (numpy, pandas, scikit-learn, etc.).
  - Established work_log.md template for progress tracking.
- Practical impact:
  - Provided organized foundation for reproducible portfolio development.
- Reflection/next action:
  - Begin implementing synthetic data generation utility next week.

### Week of 2026-01-26

- Task:
  - Implement synthetic data generation utility for student engagement dataset.
- Changes made:
  - Created src/data_generation.py with DatasetConfig class and generate_student_dataset function.
  - Generated initial dataset with features: weekly_logins, avg_session_minutes, etc., and dropout_risk target.
- Practical impact:
  - Enabled consistent synthetic data for all notebooks, avoiding real data privacy issues.
- Reflection/next action:
  - Start developing Notebook 01 for classical ML foundations.

### Week of 2026-02-02

- Task:
  - Develop Notebook 01: Classical ML Foundations, covering K-Means, KNN, and SVM.
- Changes made:
  - Implemented data loading, preprocessing, and exploratory analysis.
  - Added K-Means clustering with elbow method and silhouette analysis.
  - Built KNN and SVM classifiers with grid search and evaluation metrics.
- Practical impact:
  - Demonstrated baseline ML techniques on engagement data, identifying retention risk patterns.
- Reflection/next action:
  - Refine Notebook 01 outputs and begin Notebook 02 for ANN.

### Week of 2026-02-09

- Task:
  - Prepare Notebook 02 structure for Artificial Neural Networks.
- Changes made:
  - Created notebook framework with imports and data loading sections.
  - Outlined ANN architecture and training workflow.
- Practical impact:
  - Established foundation for neural network implementation.
- Reflection/next action:
  - Implement full ANN model with diagnostics.

### Week of 2026-02-16

- Task:
  - Set up Notebook 03 for Deep Learning techniques.
- Changes made:
  - Created notebook with environment checks for TensorFlow.
  - Prepared sections for CNN, RNN, LSTM, and Transformer approaches.
- Practical impact:
  - Prepared for advanced deep learning implementations.
- Reflection/next action:
  - Begin Notebook 04 for Reinforcement Learning.

### Week of 2026-02-23

- Task:
  - Develop Notebook 04: Reinforcement Learning Introduction.
- Changes made:
  - Implemented basic environment simulation for student engagement decisions.
  - Added policy evaluation and introductory RL concepts.
- Practical impact:
  - Introduced RL framework for future policy optimization in retention strategies.
- Reflection/next action:
  - Complete preliminary submission documentation.

### Week of 2026-03-02

- Task:
  - Refine Notebook 01 outputs and add comparative analysis.
- Changes made:
  - Enhanced visualizations and saved figures to results/figures/.
  - Added model comparison table and interpretation sections.
- Practical impact:
  - Improved clarity of classical ML results for portfolio presentation.
- Reflection/next action:
  - Expand Notebook 02 with full ANN implementation.

### Week of 2026-03-09

- Task:
  - Develop ANN baseline implementation in Notebook 02.
- Changes made:
  - Implemented scikit-learn MLPClassifier baseline with standardized inputs.
  - Added train/test evaluation using classification report.
- Practical impact:
  - Provided neural baseline for retention prediction.
- Reflection/next action:
  - Complete deep learning sections in Notebook 03.

### Week of 2026-03-16

- Task:
  - Prepare Notebook 03 deep learning structure and environment checks.
- Changes made:
  - Added TensorFlow availability check and runtime notes.
  - Structured planned sections for CNN, LSTM, and transformer-style sequence modeling.
- Practical impact:
  - Documented feasible deep learning scope for final submission environment.
- Reflection/next action:
  - Finalize all notebooks and prepare for final submission.

### Week of 2026-03-23

- Task:
  - Complete documentation and prepare preliminary submission.
- Changes made:
  - Updated README and notebook headers/objectives for consistency across portfolio artifacts.
  - Ensured all notebooks have headers and objectives.
- Practical impact:
  - Preliminary package clearly shows completed Notebook 01 and in-progress scope for Notebooks 02-04.
- Reflection/next action:
  - Address feedback and finalize for end-of-semester submission.

### Week of 2026-03-30

- Task:
  - Expand Notebook 01 to compare synthetic and real data, then rerun with current outputs.
- Changes made:
  - Downloaded UCI Student Performance dataset (`data/raw/student-mat.csv`).
  - Added real-data preprocessing and tuned KNN/SVM workflow in Notebook 01.
  - Saved processed real dataset to `data/processed/student_performance_real_processed.csv`.
  - Recorded comparison metrics:
    - Real KNN accuracy `0.570`, ROC-AUC `0.485`.
    - Real SVM accuracy `0.709`, ROC-AUC `0.702`.
    - Synthetic KNN accuracy `0.533`, ROC-AUC `0.440`.
    - Synthetic SVM accuracy `0.617`, ROC-AUC `0.416`.
  - Saved `results/figures/01_synthetic_vs_real_comparison.png`.
  - Regenerated dataset and saved to `data/processed/student_retention_dataset_v2.csv`.
  - Rerun outputs:
    - K-Means silhouette (k=3): `0.099`.
    - Best params: KNN `{n_neighbors: 3, weights: uniform}`, SVM `{C: 5.0, kernel: rbf}`.
    - Test metrics table: KNN accuracy `0.533`, ROC-AUC `0.440`; SVM accuracy `0.617`, ROC-AUC `0.416`.
- Practical impact:
  - Added a clear synthetic-vs-real baseline comparison and refreshed reproducible Notebook 01 outputs.
- Reflection/next action:
  - Proceed to ANN improvements in Notebook 02.

### Week of 2026-04-06

- Task:
  - Upgrade and rerun Notebook 02 ANN baseline with architecture comparison.
- Changes made:
  - Tested architectures: `(16,)`, `(32, 16)`, `(64, 32)`.
  - Selected best by ROC-AUC: `(32, 16)` with ROC-AUC `0.562`.
  - Reported best-model metrics: test accuracy `0.675`, minority-class F1 `0.05`, train-test gap `0.002`.
  - Saved `results/figures/02_ann_diagnostics.png`.
- Practical impact:
  - Established a stronger ANN baseline and documented diagnostics for model behavior.
- Reflection/next action:
  - Continue with deep learning implementation in Notebook 03.

### Week of 2026-04-13

- Task:
  - Upgrade Notebook 03 from placeholder to a conditional deep-learning workflow.
- Changes made:
  - Implemented conditional execution path for deep learning sections.
- Practical impact:
  - Preserved notebook usability by making execution behavior explicit for the active environment.
- Reflection/next action:
  - Complete RL notebook and consolidate documentation for submission readiness.

### Week of 2026-04-20

- Task:
  - Upgrade Notebook 04 with Q-learning, rerun results, and complete documentation review.
- Changes made:
  - Implemented and reran Q-learning workflow in Notebook 04.
  - Reported performance: learned policy mean reward `4.700` vs random policy `2.029`.
  - Saved `results/figures/04_q_learning_results.png`.
  - Consolidated documentation and completed submission-readiness review.
- Practical impact:
  - Finalized reinforcement learning evidence and improved overall portfolio coherence.
- Reflection/next action:
  - Prepare final submission package and presentation narrative.
