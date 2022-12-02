# 01모듈에서 받아온 데이터를 번호값 제외한 모든 데이터를 csv 파일에 담기
from cx_Oracle import connect

con = connect("danieldb/1@192.168.123.102:1521/xe")
cur = con.cursor()
sql="select sl_place_name, sl_phone, sl_x, sl_y from search_location order by sl_no"
cur.execute(sql)

with open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/location.csv","a",encoding="UTF-8")as f:
    for pn,ph,x,y in cur:
        f.write(f"{pn},{ph},{x},{y}\n")
con.close()
print("끝")
        