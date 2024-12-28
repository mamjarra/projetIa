import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Charger le modèle
with open('malware_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Titre de l'application
st.title('🔍 Détection de Programmes Malveillants')

# Description
st.write("""
Cette application utilise un modèle d'apprentissage automatique pour prédire si un fichier est **légitime (1)** ou **malveillant (0)** en fonction de ses caractéristiques.
""")

# Entrée des caractéristiques
st.sidebar.header('🛠️ Paramètres des Caractéristiques')

def user_input_features():
    AddressOfEntryPoint = st.sidebar.number_input('AddressOfEntryPoint', min_value=0, max_value=1000000, value=10407)
    MajorLinkerVersion = st.sidebar.number_input('MajorLinkerVersion', min_value=0, max_value=255, value=9)
    MajorImageVersion = st.sidebar.number_input('MajorImageVersion', min_value=0, max_value=1000, value=6)
    MajorOperatingSystemVersion = st.sidebar.number_input('MajorOperatingSystemVersion', min_value=0, max_value=1000, value=6)
    DllCharacteristics = st.sidebar.number_input('DllCharacteristics', min_value=0, max_value=65535, value=33088)
    SizeOfStackReserve = st.sidebar.number_input('SizeOfStackReserve', min_value=0, max_value=33554432, value=262144)
    NumberOfSections = st.sidebar.number_input('NumberOfSections', min_value=1, max_value=40, value=4)
    ResourceSize = st.sidebar.number_input('ResourceSize', min_value=0, max_value=4294967295, value=952)
    
    data = {
        'AddressOfEntryPoint': AddressOfEntryPoint,
        'MajorLinkerVersion': MajorLinkerVersion,
        'MajorImageVersion': MajorImageVersion,
        'MajorOperatingSystemVersion': MajorOperatingSystemVersion,
        'DllCharacteristics': DllCharacteristics,
        'SizeOfStackReserve': SizeOfStackReserve,
        'NumberOfSections': NumberOfSections,
        'ResourceSize': ResourceSize
    }
    return pd.DataFrame([data])

input_data = user_input_features()

# Affichage des données saisies
st.write("### Données saisies :")
st.write(input_data)

# Prédiction
if st.button('🔮 Prédire'):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    
    st.subheader('Résultat de la Prédiction')
    if prediction[0] == 1:
        st.success('✅ Le fichier est **LÉGITIME**')
    else:
        st.error('❌ Le fichier est **MALVEILLANT**')

    st.subheader('Probabilités de Prédiction')
    st.write(f'Probabilité Malveillant: {prediction_proba[0][0]:.2f}')
    st.write(f'Probabilité Légitime: {prediction_proba[0][1]:.2f}')
