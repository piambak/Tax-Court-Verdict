import numpy as np
import pandas as pd
import streamlit as st 
from sklearn import preprocessing
import pickle

model = pickle.load(open('final-model.pkl', 'rb'))
encoder_dict = pickle.load(open('encoder.pkl', 'rb')) 
cols=['age','workclass','education','marital-status','occupation','relationship','race','gender','capital-gain','capital-loss',
      'hours-per-week','native-country']    
  
def main(): 
    st.title("Income Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Income Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    Tahun Pajak = st.text_input("Tahun Pajak","0")
    Tahun Putusan = st.text_input("Tahun Putusan","0")
    Jenis Pajak = st.selectbox("Jenis Pajak", ["PPN & PPnBM", "Bea & Cukai", "PPh Badan", "Pajak Daerah", "PPh Pasal 26", "PPh Pasal 23", "PPh Pasal 4 Ayat (2)", "PPh Pasal 21", "Gugatan", "PBB", "PPh Orang Pribadi", "PPh Pasal 22", "PPh Pasal 15", "PPh Pasal 25", "Lainnya", "BPHTB"]) 
    Jenis Gugatan = st.selectbox("Education",["Banding","Peninjauan Kembali","Gugatan"]) 
    Hakim Ketua = st.selectbox("Occupation",["Dr. H. Yulius, S.H., M.H.","Drs. R. Arief Boediman, S.H., M.M., M.H.","Widayatno Sastrohardjono, S.H., M.Sc.","Dr. H. M. Hary Djatmiko, S.H., M.S.","Dr. Irfan Fachruddin, S.H., C.N.","Dr. Triyono Martanto, 5.H., 5.E., Ak., M.M., M.","IGN Mayun Winangun, S.H., L.L.M.","Wishnoe Saleh Thaib, S.H., M .H., M.Sc., Ak., CA.","Ali Hakim, S.H., SE., Ak., Msi., Ca.","Widayatno Sastrohardjono, S.H., S.Mc."]) 
    
    if st.button("Predict"): 
        features = [[tahun_pajak,tahun_putusan,jenis_pajak,jenis_gugatan,ketua]]
        data = {'Tahun Pajak': int(tahun_pajak), 'Tahun Putusan': int(tahun_putusan), 'Jenis Pajak': jenis_pajak, 'Jenis_gugatan': jenis_gugatan, 'Hakim Ketua': ketua}
        print(data)
        df=pd.DataFrame([list(data.values())], columns=['age','workclass','education','maritalstatus','occupation','relationship','race','gender','capitalgain','capitalloss','hoursperweek','nativecountry'])
                
        category_col =['workclass', 'education', 'maritalstatus', 'occupation', 'relationship', 'race', 'gender', 'nativecountry']
        for cat in encoder_dict:
            for col in df.columns:
                le = preprocessing.LabelEncoder()
                if cat == col:
                    le.classes_ = encoder_dict[cat]
                    for unique_item in df[col].unique():
                        if unique_item not in le.classes_:
                            df[col] = ['Unknown' if x == unique_item else x for x in df[col]]
                    df[col] = le.transform(df[col])
            
        features_list = df.values.tolist()      
        prediction = model.predict(features_list)
    
        output = int(prediction[0])
        if output == 1:
            text = ">50K"
        else:
            text = "<=50K"

        st.success('Employee Income is {}'.format(text))
      
if __name__=='__main__': 
    main()
