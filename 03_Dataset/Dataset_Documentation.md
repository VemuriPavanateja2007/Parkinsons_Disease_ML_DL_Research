# Dataset Documentation

> Fill this in during Phase 10 (Dataset Selection) and Phase 11 (Data Audit).

## 1. Identification
- **Dataset name:**
- **Source / link:**
- **License:**
- **Citation:**

## 2. Essential Requirements Checklist (Phase 10)
- [ ] Parkinson's labels present
- [ ] Control labels present
- [ ] Subject IDs present  ← **critical**: without this, subject-level validation is not possible
- [ ] Number of participants documented
- [ ] Number of recordings documented
- [ ] Recording conditions documented
- [ ] Language documented
- [ ] Medication information available (if any)
- [ ] Disease severity (e.g., UPDRS/H&Y) available (if any)
- [ ] Raw audio available
- [ ] Pre-extracted acoustic features available

## 3. Dataset-Level Audit (Phase 11)
| Item | Value / Notes |
|---|---|
| Number of subjects | |
| Number of recordings | |
| Class distribution (PD vs. Control) | |
| Missing values | |
| Duplicate records | |
| Feature distributions (summary) | |
| Outliers | |

## 4. Subject-Level Structure
```
Subject A
├── Recording 1
├── Recording 2
└── Recording N
```
Confirm: all recordings from a subject stay together in any split (train/val/test or CV fold).

## 5. Known Limitations
-

## 6. Decision
- [ ] Dataset selected — supports RQ1–RQ5
- [ ] Dataset rejected — reason:
