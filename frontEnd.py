import requests
import streamlit as st
from streamlit_lottie import st_lottie

import tensorflow as tf
import keras 
from PIL import Image
import io
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import subprocess

st.set_page_config(page_title="AIML-LSRS", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
	r=requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_1kHda4nbr8.json")

#img_thumbnail= Image.open("images/thumbnail.png")

logo= Image.open("Logo_Img.png")
raghav=Image.open("raghav.jpeg")
rishika=Image.open("rishika.jpeg")
sarthak=Image.open("sarthak.png")
divjot=Image.open("divjot.jpeg")
ammar=Image.open("ammar.png")
with st.container():
    left_column,right_column = st.columns([5,1])
    with left_column:
        st.subheader("Welcome to AI-ML Learning Style Recommender System!")
    with right_column:
        st.image(logo)

with st.container():
	st.title("SKILLSENSE -- Learning Style Recommender System ")

with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("Objective : ")
		st.write("##")
		st.write("""The proposed system depends on an AI classification algorithm to identify students 
        learning styles automatically using a data-driven approach.
        It will display student learning styles in four different parameters based on student behaviour patterns.\n
        The four parameters are:\n
        1. Sensitive/ Intuitive \n
        2. Active / Reflective \n
        3. Visual / Verbal \n
        4. Sequential / global""")

	with right_column:
		st_lottie(lottie_coding, height=300, key="aiml")

st.write("---")


# Define the Streamlit app

def main():
    st.title("ENTER RATINGS/OUTPUTS : ")
    st.header("ON THE BASIS OF FOCUS OF THE LEARNER (IN THE RANGE OF 0 TO 9)")

    col1, col2 = st.columns(2)

    with col1:
          ABC = st.text_input("area before content :")
          C = st.text_input("detailed content :")
          AAC = st.text_input("area after content( summaries, revision exercises) :")
          ABC_T = st.text_input("time on area before content :")
          C_T = st.text_input("time spent on detailed content :")
          AAC_T = st.text_input("time spent on area after content(summaries, revision exercises) :")

    with col2:
          D = st.text_input("definitions :")
          A = st.text_input("activity questions :")
          V = st.text_input("content pages with visual illustrations :")
          D_T = st.text_input("time spent on definitions :")
          A_T = st.text_input("time spent on activity questions:")


    # Button to evaluate
    if st.button("Evaluate"):
        # Validate input and process the numbers
        if validate_input(ABC, D, C, A, AAC, V, ABC_T, D_T, C_T, A_T, AAC_T):
            process_numbers(ABC, D, C, A, AAC, V, ABC_T, D_T, C_T, A_T, AAC_T)

def validate_input(ABC, D, C, A, AAC, V, ABC_T, D_T, C_T, A_T, AAC_T):
    # Check if all three numbers are entered
    if ABC =="" or D=="" or C=="" or A=="" or AAC=="" or V=="" or ABC_T=="" or D_T=="" or C_T=="" or A_T=="" or AAC_T=="":
        st.error("Please enter all parameters")
        return False

    # You can add additional validation rules here

    return True

def process_numbers(ABC, D, C, A, AAC, V, ABC_T, D_T, C_T, A_T, AAC_T):
    # Store the numbers as strings
    a = str(ABC)
    b = str(D)
    c = str(C)
    d = str(A)
    e = str(AAC)
    f = str(V)
    g = str(ABC_T)
    h = str(D_T)
    i = str(C_T)
    j = str(A_T)
    k = str(AAC_T)

    # Define the command to call the JavaScript file
    command = ['node', 'test0.js',a,b,c,d,e,f,g,h,i,j,k]

    # Call the JavaScript file and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    st.write("---")
    st.header("Learning Style : ")
    # Print the output of the JavaScript script
    st.write(result.stdout)

if __name__ == "__main__":
    main()
st.write("---")

st.title("Sentiment Analysis :")
st.header("Student's Facial expression will be captured and analyzed.")

if st.button("Open Camera"):
    # Call the Python file when the button is clicked
    subprocess.run(["python", "TRAIVIS_SENTIMENTALANALYSIS/mainfile.py"])


st.write("---")
st.title("ABOUT US :  ")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.image(raghav,  width=250, caption="Raghav Bohra")
with c2:
    st.image(rishika,  width=250, caption="Rishika Bhalla")
with c3:
    st.image(sarthak,  width=250, caption="Sarthak Rathore")
with c4:
    st.image(divjot, width=250, caption="Divjot Kaur")
        
st.write(" We all are pre final year students, doing our BTech in Computer Science with specialization in AI & ML, from UPES, Dehradun.")
st.write("[UPES Official Website >](https://www.upes.ac.in/)")
st.write("[TRAIVIS Official Website >](https://www.traivis.org/)")

st.write("This Project is completed under the guidance of *Mr. Ammar Hussein (Founder of TRAIVIS - Training Vision)*")
st.image(ammar, width=250, caption="Mr. Ammar Hussein")




with st.container():
	st.write("---")
	st.write("<h1 style='text-align: center;'>Thank You For Visiting...</h1>", unsafe_allow_html=True)



