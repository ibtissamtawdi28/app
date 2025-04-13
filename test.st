import streamlit as st
st.title("Ma première application Streamlit")
st.write("Bienvenue dans ce cours !")
nom = st.text_input("Quel est votre nom ?")
if nom:
    st.success(f"Enchanté, {nom} ! ")
age = st.slider("Quel est votre âge ?", 0, 100, 25)
st.write(f"Vous avez {age} ans")
genre = st.radio("Quel est votre genre ?", ["Homme", "Femme"])
st.write(f"Genre choisi : {genre}")
if st.button("Cliquez ici"):
    st.balloons()
import pandas as pd
import numpy as np
df = pd.DataFrame(
np.random.randn(10, 3),
columns=['Colonne A', 'Colonne B', 'Colonne C']
)
st.subheader("Tableau de données")
st.dataframe(df)
st.subheader("Graphique en courbes")
st.line_chart(df)

uploaded_file = st.file_uploader("Chargez un fichier CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :")
    st.dataframe(df.head())
    st.write("Statistiques descriptives :")
    st.write(df.describe())
    colonne = st.selectbox("Choisissez une colonne numérique :",df.select_dtypes(include=np.number).columns)
    st.line_chart(df[colonne])
