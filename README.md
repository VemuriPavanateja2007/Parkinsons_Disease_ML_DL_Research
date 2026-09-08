# Parkinson's Disease Detection Using Machine Learning & Deep Learning

Research workspace, set up per **Phase 0** of the research roadmap.

## Research Goal
Develop a reliable, explainable, and patient-aware ML/DL framework for voice-based Parkinson's
disease detection, comparing classical machine-learning approaches with deep-learning approaches
while addressing data leakage, overfitting, generalization, explainability, feature/representation
stability, class imbalance, and model calibration.

## Golden Rule
Do not start by building a model. Start by finding a research gap.

## Folder Guide

| Folder | Purpose | Fill in during |
|---|---|---|
| `01_Research_Idea/` | Problem statement, research questions, objectives | Phase 7–9 |
| `02_Literature_Review/` | Papers, literature matrix, research gaps | Phase 4–6 |
| `03_Dataset/` | Raw/processed data, dataset documentation | Phase 10–11 |
| `04_Preprocessing/` | Notebooks, feature engineering, audio processing scripts | Phase 12 |
| `05_Models/` | Classical ML, deep learning, pretrained model code | Phase 13–14 |
| `06_Experiments/` | One subfolder per experiment (E1–E9 in the roadmap) | Phase 15–20 |
| `07_Results/` | Tables, figures, statistical analysis outputs | Phase 17–19 |
| `08_Paper/` | Paper drafts | Phase 23 |
| `09_Journal/` | Journal comparison, submission checklist, reviewer responses | End |
| `Research_Log.md` | Dated log of decisions and findings | Ongoing |

## 14-Week Plan (from the roadmap)

| Week | Main Work |
|---|---|
| 1 | Parkinson's disease fundamentals |
| 2 | Voice modality + ML/DL fundamentals |
| 3 | Literature search |
| 4 | Literature matrix |
| 5 | Research gap + problem formulation |
| 6 | Dataset selection + proposal |
| 7 | Data audit + subject-level splitting |
| 8 | Classical ML baseline |
| 9 | MLP/DNN + CNN |
| 10 | LSTM/GRU + advanced DL |
| 11 | Robust validation + ML/DL comparison |
| 12 | Explainability + stability + calibration |
| 13 | Statistical analysis + results |
| 14 | Manuscript + journal preparation |

## First 7 Activities (Phase 25 — start here)
1. Learn Parkinson's disease fundamentals.
2. Understand why voice can contain Parkinson's-related information.
3. Learn the difference between feature-based ML vs. Deep Learning.
4. Read 10–15 important papers.
5. Create the literature matrix (`02_Literature_Review/Literature_Matrix.xlsx`).
6. Identify the actual research gap (`02_Literature_Review/Research_Gaps.docx`).
7. Select the dataset only after checking it supports the research questions —
   especially subject IDs and raw audio availability (`03_Dataset/Dataset_Documentation.md`).

## Recommended Working Title
"Reliable and Explainable Machine Learning and Deep Learning for Voice-Based Parkinson's Disease
Detection Using Subject-Level Validation and Representation Stability Analysis."

## Central Research Philosophy
ML baseline → DL models → patient-aware validation → representation comparison → explainability →
stability → calibration → external validation.
