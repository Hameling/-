import pymysql
import hash
 
faddress = hash.dige
fname = "filename"
fowner = "groupname"
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='',
                       db='testdata', charset='utf8')
 

# Connection 으로부터 Cursor 생성
cur = conn.cursor()
 
# SQL문 실행
#cur.execute("insert into savefile(faddress,fname,fowner) VALUES(%s,%s,%s)",(faddress,fname,fowner))

cur.execute("select * from savefile where faddress = %s",faddress)
conn.commit()

# 전체 rows
for row in cur.fetchall():
    print(row)
 
# Connection 닫기
conn.close()