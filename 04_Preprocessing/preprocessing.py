"""
preprocessing.py
Parkinson's Disease ML/DL Research — Preprocessing entry point.

Fill this in during Phase 12 (Preprocessing), AFTER Phase 11 (Data Audit).

Rules to keep, per the roadmap:
- Subject-level split happens BEFORE any scaling/imputation/feature selection.
- Fit scalers/imputers/feature selectors on TRAINING data only, within each fold.
- No augmentation on validation or test data.
"""

# ---------------------------------------------------------------------------
# 1. Load raw data (from ../03_Dataset/Raw_Data/)
# ---------------------------------------------------------------------------
def load_raw_data():
    raise NotImplementedError("Load dataset once selected in Phase 10.")


# ---------------------------------------------------------------------------
# 2. Subject-level split (GroupKFold / Leave-One-Subject-Out)
# ---------------------------------------------------------------------------
def subject_level_split(df, subject_col="subject_id"):
    """
    All recordings from a given subject must stay in the same split.
    Use sklearn.model_selection.GroupKFold or LeaveOneGroupOut with
    groups=df[subject_col].
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 3. Classical ML preprocessing path
#    Raw -> Missing Value Handling -> Feature Scaling -> Feature Selection
# ---------------------------------------------------------------------------
def preprocess_for_ml(train_df, test_df):
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 4. Deep learning (audio) preprocessing path
#    Raw Audio -> Quality Check -> Resampling -> Normalization ->
#    Segmentation -> Spectrogram/Mel-Spectrogram -> (train-only) Augmentation
# ---------------------------------------------------------------------------
def preprocess_for_dl_audio(train_files, test_files):
    raise NotImplementedError


if __name__ == "__main__":
    print("Preprocessing pipeline stub — implement after dataset selection (Phase 10).")
