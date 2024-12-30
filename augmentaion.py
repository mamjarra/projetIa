from imblearn.over_sampling import SMOTE
import pandas as pd

# Charger les données
file_path = "DatasetmalwareExtrait.csv"
data = pd.read_csv(file_path)
X = data.drop('legitimate', axis=1)
y = data['legitimate']

# Appliquer SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Sauvegarder les données augmentées
augmented_path = "dataset_augmented.csv"
pd.concat([X_resampled, y_resampled], axis=1).to_csv(augmented_path, index=False)
print(f"Dataset augmenté sauvegardé à : {augmented_path}")
