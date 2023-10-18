import pymysql
class DaoMem:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                           db='python',port=3304, charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = """
        select 
        M_ID, M_NM, TEL, ADDRESS 
        from MEM
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list

    def selectOne(self,m_id):
        sql = f"""
        select
            M_ID, M_NM, TEL, ADDRESS 
        FROM MEM
        WHERE
            M_ID = '{m_id}'
        """
        self.curs.execute(sql)
        mem = self.curs.fetchall()
        return mem[0]
    
    def insert(self,m_id,m_nm,tel,address):
        sql = f"""
        insert into MEM
            (M_ID, M_NM, TEL, ADDRESS)
        values
            ('{m_id}','{m_nm}','{tel}','{address}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,m_id,m_nm,tel,address):
        sql = f"""
        update MEM
        set
            M_NM = '{m_nm}',
            TEL = '{tel}',
            ADDRESS = '{address}'
        where
            M_ID = '{m_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,m_id):
        sql = f"""
        delete from MEM
        where
            m_id = '{m_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
    