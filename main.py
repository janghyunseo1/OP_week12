import streamlit as st
import pandas as pd

st.subheader('csv 파일 업로드 ')

uploaded_file = st.file_uploader('CSV 파일 업로드', type=['csv'])

print(uploaded_file)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("업로드 된 CSV 파일의 정보")
    st.dataframe(df)
    
else:
    st.write("CSV 파일을 업로드 하세요.")