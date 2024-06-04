import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the pkl file
with open('final-model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the data
df = pd.read_csv('cropped.csv')

# Create a title and description
st.title('Machine Learning Dashboard')
st.markdown('This dashboard uses a machine learning model to predict outcomes.')

# Create filters for the control variables
tahun_pajak_filter = st.selectbox("Select Tahun Pajak", pd.unique(df["tahun_pajak"]))
tahun_putusan_filter = st.selectbox("Select Tahun Putusan", pd.unique(df["tahun_putusan"]))
jenis_pajak_filter = st.selectbox("Select Jenis Pajak", pd.unique(df["jenis_pajak"]))
jenis_gugatan_filter = st.selectbox("Select Jenis Gugatan", pd.unique(df["jenis_gugatan"]))
ketua_filter = st.selectbox("Select Ketua", pd.unique(df["ketua"]))

# Filter the data
df = df[(df["tahun_pajak"] == tahun_pajak_filter) &
        (df["tahun_putusan"] == tahun_putusan_filter) &
        (df["jenis_pajak"] == jenis_pajak_filter) &
        (df["jenis_gugatan"] == jenis_gugatan_filter) &
        (df["ketua"] == ketua_filter)]

# Create KPIs/summary cards
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="Mean Hasil Putusan", value=df["hasil_putusan"].mean())
kpi2.metric(label="Count", value=df.shape[0])
kpi3.metric(label="Hasil Putusan Distribution", value=df["hasil_putusan"].value_counts())

# Create a data table
st.markdown("### Detailed Data View")
st.dataframe(df)

# Create a prediction function
def predict(input_data):
    return model.predict(input_data)

# Create a form to input data
st.markdown("### Make a Prediction")
with st.form("prediction_form"):
    tahun_pajak = st.number_input("Tahun Pajak")
    tahun_putusan = st.number_input("Tahun Putusan")
    jenis_pajak = st.selectbox("Jenis Pajak", pd.unique(df["jenis_pajak"]))
    jenis_gugatan = st.selectbox("Jenis Gugatan", pd.unique(df["jenis_gugatan"]))
    ketua = st.selectbox("Ketua", pd.unique(df["ketua"]))
    submit_button = st.form_submit_button("Make Prediction")

    if submit_button:
        input_data = pd.DataFrame({'tahun_pajak': [tahun_pajak], 
                                   'tahun_putusan': [tahun_putusan], 
                                   'jenis_pajak': [jenis_pajak], 
                                   'jenis_gugatan': [jenis_gugatan], 
                                   'ketua': [ketua]})
        prediction = predict(input_data)
        st.write("Prediction:", prediction)
