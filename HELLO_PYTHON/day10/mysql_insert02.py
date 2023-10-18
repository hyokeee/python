import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python',port=3304, charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
# 방법1
# sql = """
# insert into emp
#     (e_id, e_name, gen, addr)
# values
#     (%s, %s, %s, %s)
# """
# my_tup = ("3","3","3","3")
# curs.execute(sql, my_tup)


#방법2
e_id = "4"
e_name = "4"
gen = "4"
addr = "4"

sql = f"""
insert into emp
    (e_id, e_name, gen, addr)
values
    ('{e_id}','{e_name}','{gen}','{addr}')
"""
cnt = curs.execute(sql)
print("cnt",cnt)
print("curs.rowcount",curs.rowcount)

# Commit
conn.commit()


# Connection 닫기
conn.close()

