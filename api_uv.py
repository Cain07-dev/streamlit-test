import requests
import pprint
import json
from datetime import datetime


def uv_process(code):
    # BaseURL
    base_url = "http://apis.data.go.kr/1360000/LivingWthrIdxServiceV3/getUVIdxV3"

    # 서비스 키
    service_Key = "?serviceKey=79q0SKoHP%2Fmpdu8C5Z1Ox9TMHKcPf8%2BsuloysjNhmPmCamXI1eunTRfE%2FNxNPomTgvCIguz%2B05jk3s43Qg71nA%3D%3D"

    # 오늘 날짜 + 00시
    cur_date = datetime.now().strftime("%Y%m%d") + "00"

    # url 입력
    url = base_url \
        + service_Key + \
        "&pageNo=1" \
        "&numOfRows=10" \
        "&dataType=JSON" \
        "&areaNo=" + str(code) +  \
        "&time=" + cur_date

    # url 불러오기
    response = requests.get(url)

    # 데이터 값 출력해보기
    contents = response.text

    # Json Parse
    js = json.loads(contents)
    res = js.get("response")
    body = res.get("body")
    items = body.get("items")
    item = items.get("item")

    item_dict = item[0]

    uv_inf = {}

    # 오늘 내일 모레의 자외선 수치를 dict에 저장하고
    # 날짜 별로 최대 자외선 수치를 리스트에 저장해서 return
    uv_today = {}
    uv_tomorrow = {}
    uv_after = {}
    max_uv_list = []

    for i in range(0, 70 + 1, 3):
        uv_key = "h" + str(i)

        uv_inf[uv_key] = int(item_dict[uv_key])

        if i <= 24:
            uv_today[uv_key] = int(item_dict[uv_key])
        elif i > 24 and i <= 48:
            uv_tomorrow[uv_key] = int(item_dict[uv_key])
        elif i > 48 and i <= 72:
            uv_after[uv_key] = int(item_dict[uv_key])

    # print(uv_inf)
    # print(uv_today)
    # print(uv_tomorrow)
    # print(uv_after)

    max_uv_list.append(max(uv_today.values()))
    max_uv_list.append(max(uv_tomorrow.values()))
    max_uv_list.append(max(uv_after.values()))
    # print(max_uv_list)

    return max_uv_list





