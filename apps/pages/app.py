import streamlit as st

st.title('나의 첫 앱')
st.write('파이썬 파일 하나가 웹 화면이 됩니다.')

age = st.slider("나이:", 40,95,60)
st.write(f"선택: {age}")