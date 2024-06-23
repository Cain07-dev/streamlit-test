import pandas as pd
# import openpyxl

def rd_excel():

    df = pd.read_excel('citycode.xlsx', engine='openpyxl')

    city_code = df['행정구역코드']

    code = []
    city = []
    target_x = []
    target_y = []


    for index, row in df.iterrows():
        df_citycode = row["행정구역코드"]

        if df_citycode % 100000000 == 0:

            df_city = row["1단계"]
            df_x = row["격자 X"]
            df_y = row["격자 Y"]

            code.append(df_citycode)
            city.append(df_city)
            target_x.append(df_x)
            target_y.append(df_y)

            # print(df_citycode, df_city, df_x, df_y)

    # print(code)
    # print(city)
    # print(target_x)
    # print(target_y)
    # print(len(code), len(city), len(target_y), len(target_x))

    return code, city, target_x, target_y

print(rd_excel())

