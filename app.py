import streamlit as st
import pickle
import pandas as pd

# Charger le modèle
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Interface utilisateur
st.title("Détection de Malware")
st.sidebar.header("Entrez les caractéristiques")

def user_input():
    AddressOfEntryPoint = st.sidebar.number_input('AddressOfEntryPoint', min_value=0, max_value=1000000, value=10407)
    MajorLinkerVersion = st.sidebar.number_input('MajorLinkerVersion', min_value=0, max_value=255, value=9)
    MajorImageVersion = st.sidebar.number_input('MajorImageVersion', min_value=0, max_value=1000, value=6)
    MajorOperatingSystemVersion = st.sidebar.number_input('MajorOperatingSystemVersion', min_value=0, max_value=1000, value=6)
    DllCharacteristics = st.sidebar.number_input('DllCharacteristics', min_value=0, max_value=65535, value=33088)
    SizeOfStackReserve = st.sidebar.number_input('SizeOfStackReserve', min_value=0, max_value=33554432, value=262144)
    NumberOfSections = st.sidebar.number_input('NumberOfSections', min_value=1, max_value=40, value=4)
    ResourceSize = st.sidebar.number_input('ResourceSize', min_value=0, max_value=4294967295, value=952)
    return pd.DataFrame([{
        "AddressOfEntryPoint": AddressOfEntryPoint,
        "MajorLinkerVersion": MajorLinkerVersion,
        "MajorImageVersion": MajorImageVersion,
        "MajorOperatingSystemVersion": MajorOperatingSystemVersion,
        "DllCharacteristics": DllCharacteristics,
        "SizeOfStackReserve": SizeOfStackReserve,
        "NumberOfSections": NumberOfSections,
        "ResourceSize": ResourceSize
    }])

input_data = user_input()
if st.button("Prédire"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Légitime")
    else:
        st.error("Malveillant")
