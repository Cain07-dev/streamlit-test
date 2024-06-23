# 날씨 정보 API 대시보드

이 프로젝트는 Streamlit을 사용하여 날씨, 자외선, 미세먼지 정보를 제공하는 대시보드입니다.

## 기능

1. 날씨 정보
   - 선택한 도시의 온도, 하늘 상태, 강수확률, 습도를 표시합니다.

2. 자외선 정보
   - 선택한 시도의 오늘과 내일의 자외선 지수를 표시합니다.
   - 자외선 지수에 따른 주의사항을 제공합니다.

3. 미세먼지 정보
   - 선택한 시도의 통합대기지수, 미세먼지(PM10), 초미세먼지(PM2.5) 상태와 수치를 표시합니다.

## 사용된 라이브러리

- streamlit
- matplotlib
- numpy
- openpyxl

## 주요 파일

- `excel_read.py`: 엑셀 파일에서 시도의 코드와 좌표를 가져옵니다.
- `api_weather.py`: 날씨 API 처리 
- `api_uv.py`: 자외선 API 처리 
- `api_dust.py`: 미세먼지 API 처리 

## 작동

엑셀파일에서 시도의 이름, 코드, 좌표를 가져옵니다.
선택된 시도의 날씨정보를 api를 사용해서 가져옵니다.

## 공공데이터 활용 (사용한 API)

날씨 정보 API

[https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15084084]

자외선 API

[https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15085288]

미세먼지 API

[https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15073861]
