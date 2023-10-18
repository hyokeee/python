import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python',port=3304, charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행
sql = "select * from emp"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows

# Connection 닫기
conn.close()