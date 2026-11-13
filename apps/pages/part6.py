import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("더하기"):
    st.session_state.count += 1
if st.button("처음으로"):
    st.session_state.count =0

st.write(f"클릭 횟수: {st.session_state.count}")

with st.form("bmi_form"):
    height = st.number_input("키", 100.0,220.0,170.0)
    weight = st.number_input("몸무게", 30.0,200.0,65.0)
    done = st.form_submit_button("계산하기")

if done:
    bmi = weight / (height/100) **2
    st.write(f"BMI: {bmi:.1f}")

import pandas as pd

DATA = "heart_failure_clinical_records_dataset.csv"

df=pd.read_csv(DATA)
low,high = st.slider("나이 범위", 40,95,(91,93))
part=df[(df["age"]>=low)&(df["age"]<=high)]

if len(part)==0:
    st.warning("조건에 맞는 환자가 없습니다.")
    st.stop()

st.write(f"평균 박출률:{part['ejection_fraction'].mean():.1f}")

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(DATA)



