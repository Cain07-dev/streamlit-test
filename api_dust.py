import requests
import json
# 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종

def dust_process(sido):
    base_url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

    service_Key = "?serviceKey=79q0SKoHP%2Fmpdu8C5Z1Ox9TMHKcPf8%2BsuloysjNhmPmCamXI1eunTRfE%2FNxNPomTgvCIguz%2B05jk3s43Qg71nA%3D%3D"

    # & returnType = json & numOfRows = 100 & pageNo = 1 & sidoName = 서울 & ver = 1.0
    url = base_url \
        + service_Key + \
        "&returnType=json" \
        "&numOfRows=1" \
        "&pageNo=1"\
        + "&sidoName=" + sido + \
        "&ver=1.3"

    # response = requests.get(base_url, params=params)

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
    item = items[0]

    # print(item)
    return item

print(dust_process('서울'))