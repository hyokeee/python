#select e_id, e_name, gen, addr from emp;
# pip install할 때 mysql 라이브러리를 깔아서 하자\
import mysql.connector
import pymysql

# MariaDB 연결 설정
config = {
    'user': 'root',
    'password': 'python',
    'host': '127.0.0.1',
    'database': 'python',
    'port': 3304,
    'raise_on_warnings': True
}

# MariaDB 연결
cnx = mysql.connector.connect(**config)

# 연결 확인
if cnx.is_connected():
    print('MariaDB에 연결되었습니다.')
    #cnx.close()
    cursor = cnx.cursor(pymysql.cursors.DictCursor)
    
    
    # 쿼리문 실행
    query = "SELECT e_id, e_name, gen, addr FROM emp"
    cursor.execute(query)

    # 결과 가져오기
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(row)

    # 커서와 연결 닫기
    cursor.close()
    cnx.close()