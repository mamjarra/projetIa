import pickle
from art.attacks.evasion import FastGradientMethod
from art.estimators.classification import SklearnClassifier
import pandas as pd

# Charger le modèle
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Charger les données
file_path = "DatasetmalwareExtrait.csv"
data = pd.read_csv(file_path)
columns_to_normalize = ['AddressOfEntryPoint', 'ResourceSize', 'SizeOfStackReserve']
X = data.drop('legitimate', axis=1)
y = data['legitimate']

# Envelopper le modèle avec ART
classifier = SklearnClassifier(model=model)

# Générer des exemples adversariaux
attack = FastGradientMethod(estimator=classifier, eps=0.1)
X_adv = attack.generate(X=X)

# Sauvegarder le dataset adversarial
adversarial_path = "dataset_adversarial.csv"
pd.DataFrame(X_adv, columns=X.columns).to_csv(adversarial_path, index=False)
print(f"Dataset adversarial sauvegardé à : {adversarial_path}")
