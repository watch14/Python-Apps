import streamlit as st
import pandas as pd

st.set_page_config(page_title="Certificates", page_icon=":book:", layout="wide")

df = pd.read_csv("assets/certificate.csv", sep=";")

for i , row in df.iterrows():
    st.header(row["title"])
    st.image(row["image"])
    st.markdown(f"[Verify Certificate]({row["url"]})")

    
    st.write("---")
