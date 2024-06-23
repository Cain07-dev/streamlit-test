import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from excel_read import rd_excel

st.title("Streamlit Test")
st.header("Barchart")

rand = np.random.normal(1,2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

code, city, target_x, target_y = rd_excel()
st.subheader(code)
st.subheader(city)
st.subheader(target_x)
st.subheader(target_y)