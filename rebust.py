import pickle
import pandas as pd
from sklearn.metrics import accuracy_score

# Charger le modèle
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Charger les datasets
file_path = "DatasetmalwareExtrait.csv"
data = pd.read_csv(file_path)
X = data.drop('legitimate', axis=1)
y = data['legitimate']

adversarial_path = "dataset_adversarial.csv"
X_adv = pd.read_csv(adversarial_path)

# Évaluer sur le jeu original
y_pred = model.predict(X)
accuracy_original = accuracy_score(y, y_pred)
print(f"Précision sur les données originales : {accuracy_original:.2f}")

# Évaluer sur le dataset adversarial
y_pred_adv = model.predict(X_adv)
accuracy_adv = accuracy_score(y, y_pred_adv)
print(f"Précision sur les données adversariales : {accuracy_adv:.2f}")

# Calculer l'écart de robustesse
robustness_gap = accuracy_original - accuracy_adv
print(f"Écart de robustesse : {robustness_gap:.2f}")
