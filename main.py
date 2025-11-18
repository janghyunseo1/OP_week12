import streamlit as st

st.title("Streamlit 기본 실습")

st.markdown("## Task 1: 기본 UI 컴포넌트")

st.text_input("이름을 입력하세요: ")

st.slider("나이", min_value=0, max_value=100, value = 25)

colors = ["빨강", "파랑","초록","노랑","검정"]
st.selectbox("좋아하는 색",colors, index = 0)

st.checkbox("이용 약관에 동의합니다.")

st.button("제출")