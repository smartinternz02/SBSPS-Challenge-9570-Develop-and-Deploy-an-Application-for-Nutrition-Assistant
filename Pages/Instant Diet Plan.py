import streamlit as st
import base64
import pandas as pd
from  PIL import Image

from streamlit_option_menu import option_menu
from streamlit_text_rating.st_text_rater import st_text_rater

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


feature_image1 = Image.open(r'C:\Users\Narendra\PycharmProjects\copy-of-git\app\pages\wt.jpeg')
with st.container():
    image_col, text_col = st.columns((1, 3))
    with image_col:
        st.image(feature_image1)
    with text_col:
        st.markdown(""" <style> .font {
        font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">DIET</p>', unsafe_allow_html=True)
        st.markdown(
            "In nutrition, diet is the sum of food consumed by a person or other organism. The word diet often implies the use of specific intake of nutrition for health or weight-management reasons. Although humans are omnivores, each culture and each person holds some food preferences or some food taboos."
        )
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('Read PDF', key='1'):
        show_pdf('diet.pdf')
with col2:
    st.button('Close PDF', key='2')
with col3:
    with open('diet.pdf', "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download PDF", key='3',
                       data=PDFbyte,
                       file_name="diet.pdf",
                       mime='application/octet-stream')

