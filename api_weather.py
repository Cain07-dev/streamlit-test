import requests, json
from datetime import datetime, timedelta


# 기본값 서울
def weather_process(x, y):
    base_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"

    service_Key = "?serviceKey=79q0SKoHP%2Fmpdu8C5Z1Ox9TMHKcPf8%2BsuloysjNhmPmCamXI1eunTRfE%2FNxNPomTgvCIguz%2B05jk3s43Qg71nA%3D%3D"

    # 오늘 날짜 가져오기
    now = datetime.now()
    today = now.date()
    current_time = datetime.now().time()

    # 현재 시간이 오전 5시 이전 일 때 어제 날짜로 변경하고 시간을 05시로 변경
    # (api 데이터 발표 시간이 05시)
    if current_time.hour < 5:
        cur_date = today - timedelta(days=1)
        cur_date = cur_date.strftime("%Y%m%d")
        hour = "0500"
    else:
        cur_date = datetime.now().strftime("%Y%m%d")
        hour = now.strftime("%H") + "00"

    print(cur_date, hour)

    url = base_url + \
          service_Key + \
          "&pageNo=1" + \
          "&numOfRows=295" + \
          "&dataType=json" + \
          "&base_date=" + cur_date + \
          "&base_time=0500" \
          "&nx=" + str(x) + "&ny=" + str(y)

    # url 불러오기
    response = requests.get(url)

    # 데이터 값 출력해보기
    contents = response.text
    # print(contents)

    # Json Parse
    js = json.loads(contents)
    res = js.get("response")
    body = res.get("body")
    items = body.get("items")
    item = items.get("item")

    weather = {}

    # 현재 시간의 날씨정보를 저장
    for i in item:
        if i["fcstTime"] == hour and i["fcstDate"] == cur_date:
            key = i["category"]
            val = i["fcstValue"]
            weather[key] = val

    # print(weather)
    return weather

print(weather_process(60, 127))


