import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 

# loading in the model to predict on the data 
pickle_in = open('final-model.pkl', 'rb') 
classifier = pickle.load(pickle_in) 

def welcome(): 
	return 'welcome all'

# defining the function which will make the prediction using 
# the data which the user inputs 
def prediction(tahun_pajak, tahun_putusan, jenis_pajak, jenis_gugatan, ketua): 

	prediction = classifier.predict( 
		[[tahun_pajak, tahun_putusan, jenis_pajak, jenis_gugatan, ketua]]) 
	print(prediction) 
	return prediction 
	

# this is the main function in which we define our webpage 
def main(): 
	# giving the webpage a title 
	st.title("Tax Verdict Prediction") 
	
	# here we define some of the front end elements of the web page like 
	# the font and background color, the padding and the text to be displayed 
	html_temp = """ 
	<div style ="background-color:yellow;padding:13px"> 
	<h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1> 
	</div> 
	"""
	
	# this line allows us to display the front end aspects we have 
	# defined in the above code 
	st.markdown(html_temp, unsafe_allow_html = True) 
	
	# the following lines create text boxes in which the user can enter 
	# the data required to make the prediction 
	tahun_pajak = st.text_input("Tahun Pajak", "Type Here")
    	tahun_putusan = st.text_input("Tahun Putusan", "Type Here")
    	jenis_pajak = st.selectbox("Jenis Pajak", pd.unique(df["jenis_pajak"]))
    	jenis_gugatan = st.selectbox("Jenis Gugatan", pd.unique(df["jenis_gugatan"]))
    	ketua = st.selectbox("Ketua", pd.unique(df["ketua"]))
    	result ="" 
	
	# the below line ensures that when the button called 'Predict' is clicked, 
	# the prediction function defined above is called to make the prediction 
	# and store it in the variable result 
	if st.button("Predict"): 
		result = prediction(tahun_pajak, tahun_putusan, jenis_pajak, jenis_gugatan, ketua) 
	st.success('The output is {}'.format(result)) 
	
if __name__=='__main__': 
	main() 
