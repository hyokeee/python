import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python',port=3304, charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
sql = "insert into emp values(%s,%s,%s,%s)"
curs.execute(sql,("3","3","3","3"))
# sql = "insert into emp values('3','3','3','3')"
# curs.execute(sql)


# Commit
conn.commit()

# Connection 닫기
conn.close()