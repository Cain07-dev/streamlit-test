import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


from excel_read import rd_excel
from api_weather import weather_process


st.title("날씨 정보 API")

code, city, target_x, target_y = rd_excel()

for i in range(len(city)):
    if city[i] == "경상북도":
        city[i] = "경북"
    elif city[i] == "경상남도":
        city[i] = "경남"
    elif city[i] == "전라북도":
        city[i] = "전북"
    elif city[i] == "전라남도":
        city[i] = "전남"
    elif city[i] == "충청북도":
        city[i] = "충북"
    elif city[i] == "충청남도":
        city[i] = "충남"
    else:
        city[i] = city[i][0:2]

city_code = {}
for i, j in zip(city, code):
    city_code[i] = j

select_city = st.selectbox("sido", city)
# 입력받은 시도의 좌표를 구하기
if select_city in city:
    index = city.index(select_city)
print(index)
input_x = target_x[index]
input_y = target_y[index]
# api 호출
weather_item = weather_process(input_x, input_y)

# 온도, 풍향, 강수확률, 습도, 하늘 상태
tmp = weather_item["TMP"]
wsd = weather_item["WSD"]
pop = weather_item["POP"]
reh = weather_item["REH"]
# 하늘 상태 변환 1: 맑음, 3:구름 많음, 4:흐림
sky = weather_item["SKY"]
if sky == "1":
    sky = "맑음"
elif sky == "3":
    sky = "구름 많음"
elif sky == "4":
    sky = "흐림"
else:
    sky = "보통"

st.subheader(tmp)
st.subheader(sky)
st.subheader(pop)