# REST API키    f141c31bd350eab39a78263860270365
# 위도경도 ?    37.4335824  127.1288568
from urllib.parse import quote
from http.client import HTTPSConnection
from json import loads
from cx_Oracle import connect



search = quote(input("검색어: "))
# print(search)

hc= HTTPSConnection("dapi.kakao.com")
url=f"/v2/local/search/keyword.json?query={search}&x=37.4335824&y=127.1288568&radius=1000"
h={"Authorization" :"KakaoAK f141c31bd350eab39a78263860270365"}

hc.request("GET", url, headers=h)

resBody=hc.getresponse().read()
# print(resBody.decode())

#---------------------DB연결-------------------#
con=connect("danieldb/1@192.168.123.102:1521/xe")
cur=con.cursor()

location = loads(resBody)

for i in location["documents"]:
    sql=f"insert into search_location values(search_location_seq.nextval,'{i['place_name']}',nvl('{i['phone']}','-'),{float(i['x']):.6f},{float(i['y']):.6f})"
    cur.execute(sql)
    # print(i["place_name"])
    # print(i["phone"])
    # print(f"{float(i['x']):.6f}")
    # print(f"{float(i['y']):.6f}")
    # # print(i["x"])
    # # print(i["y"])
    # print("----------------")
    
con.commit()
con.close()
hc.close()