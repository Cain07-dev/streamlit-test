import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


from excel_read import rd_excel
from api_weather import weather_process
from api_uv import uv_process
from api_dust import dust_process

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


# weather api
weather_city = st.selectbox("weather", city)
# 입력받은 시도의 좌표를 구하기
if weather_city in city:
    index = city.index(weather_city)
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

st.subheader(f"온도: {tmp}")
st.subheader(f"하늘 상태: {sky}")
st.subheader(f"강수확률: {pop}")
st.subheader(f"습도: {reh}")

# uv api
uv_city = st.selectbox("uv", city)
# 입력받은 시도의 지역코드 가져오기
input_code = city_code[uv_city]
# api 호출해서 오늘, 내일, 모레의 최대 자외선 리스트 가져오기
max_uv_num = uv_process(input_code)
# st.subheader(max_uv_num)
# 자외선 지수에 따라서 문구 작성, 이미지 경로 설정
if max_uv_num[0] >= 11:
    today_uv = "위험"
    today_script = "외출을 피하고 실내에 머무세요"
elif max_uv_num[0] >= 8:
    today_uv = "매우 높음"
    today_script = "한낮에 장시간 외출을 피하세요"
elif max_uv_num[0] >= 6:
    today_uv = "높음"
    today_script = "낮에는 그늘에서 머무세요"
elif max_uv_num[0] >= 3:
    today_uv = "보통"
    today_script = "외출 할때는 자외선 차단제를 발라주세요"
else:
    today_uv = "낮음"
    today_script = ""
if max_uv_num[1] >= 11:
    tomorrow_uv = "위험"
    tomorrow_script = "외출을 피하고 실내에 머무세요"
elif max_uv_num[1] >= 8:
    tomorrow_uv = "매우 높음"
    tomorrow_script = "한낮에 장시간 외출을 피하세요"
elif max_uv_num[1] >= 6:
    tomorrow_uv = "높음"
    tomorrow_script = "한낮에 장시간 외출을 피하세요"
elif max_uv_num[1] >= 3:
    tomorrow_uv = "보통"
    tomorrow_script = "외출 할때는 자외선 차단제를 발라주세요"
else:
    tomorrow_uv = "낮음"
    tomorrow_script = ""

st.subheader(f"오늘의 자외선 지수: {today_uv}")
st.caption(today_script)
st.subheader(f"내일의 자외선 지수: {tomorrow_uv}")
st.caption(tomorrow_script)


# 미세먼지 수치
dust_city = st.selectbox("dust", city)
# api 호출
dust_item = dust_process(dust_city)

# 통합대기지수
khaiGrade = dust_item["khaiGrade"]

if (khaiGrade == '1'):
    khaiGrade = "좋음"
elif (khaiGrade == '2'):
    khaiGrade = "보통"
elif (khaiGrade == '3'):
    khaiGrade = "나쁨"
elif (khaiGrade == '4'):
    khaiGrade = "매우 나쁨"

# pm10 미세먼지 지수, 수치
pm10_grade = dust_item["pm10Grade"]
pm25_grade = dust_item["pm25Grade"]

if (pm10_grade == '1'):
    pm10_grade = "좋음"
elif (pm10_grade == '2'):
    pm10_grade = "보통"
elif (pm10_grade == '3'):
    pm10_grade = "나쁨"
elif (pm10_grade == '4'):
    pm10_grade = "매우 나쁨"
else:
    pm10_grade = "None"

# pm25 초미세먼지 지수, 수치
if (pm25_grade == '1'):
        pm25_grade = "좋음"
elif (pm25_grade == '2'):
    pm25_grade = "보통"
elif (pm25_grade == '3'):
    pm25_grade = "나쁨"
elif (pm25_grade == '4'):
    pm25_grade = "매우 나쁨"
else:
    pm25_grade = "None"

pm10_val = dust_item["pm10Value"]
pm25_val = dust_item["pm25Value"]

st.subheader(f"오늘 {dust_city}의 대기상태는 {khaiGrade}")
st.subheader(f"미세먼지(pm10) 상태: {pm10_grade}")
st.subheader(f"미세먼지(pm10) 수치: {pm10_val}")
st.subheader(f"미세먼지(pm25) 상태: {pm25_grade}")
st.subheader(f"미세먼지(pm25) 수치: {pm25_val}")