import streamlit as st
import pandas as pd

DATA = "heart_failure_clinical_records_dataset.csv"
df = pd.read_csv(DATA)

st.title("심부전 환자 차트")
counts =df["DEATH_EVENT"].map({0:"생존", 1:"사망"}).value_counts()
st.bar_chart(counts)

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

fm.fontManager.addfont("NanumGothic-Regular.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

fig, ax= plt.subplots()
ax.bar(counts.index, counts.values)
ax.set_title("사망 여부별 환자 수")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(df["age"], bins=11, range=(40,95), color="#2E6B47")
ax.set_xlabel("나이")
ax.set_ylabel("환자 수")
st.pyplot(fig)

import seaborn as sns

