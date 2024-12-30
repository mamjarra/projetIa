# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score
# import pickle

# # Chargement des données
# file_path = "../data/DatasetmalwareExtrait.csv"
# data = pd.read_csv(file_path)

# # Normalisation
# columns_to_normalize = ['AddressOfEntryPoint', 'ResourceSize', 'SizeOfStackReserve']
# scaler = StandardScaler()
# data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize])

# # Séparation en X et y
# X = data.drop('legitimate', axis=1)
# y = data['legitimate']

# # Division des données
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Entraînement du modèle
# model = RandomForestClassifier(random_state=42)
# model.fit(X_train, y_train)

# # Évaluation
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Précision sur le jeu de test : {accuracy:.2f}")

# # Sauvegarde du modèle
# model_path = "../models/malware_model.pkl"
# with open(model_path, 'wb') as file:
#     pickle.dump(model, file)
# print(f"Modèle sauvegardé à : {model_path}")
