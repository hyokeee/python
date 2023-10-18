import pymysql
class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                           db='python',port=3304, charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = """
        select 
        E_ID, E_NAME, GEN, ADDR 
        from emp
        ORDER BY CAST(E_ID AS INTEGER)
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list

    def selectOne(self,e_id):
        sql = f"""
        select
            E_ID, E_NAME, GEN, ADDR
        FROM EMP
        WHERE
            E_ID = '{e_id}'
        """
        self.curs.execute(sql)
        emp = self.curs.fetchall()
        return emp[0]
    
    def insert(self,e_id,e_name,gen,addr):
        sql = f"""
        insert into emp
            (e_id, e_name, gen, addr)
        values
            ('{e_id}','{e_name}','{gen}','{addr}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,e_id,e_name,gen,addr):
        sql = f"""
        update emp
        set
            e_name = '{e_name}',
            gen = '{gen}',
            addr = '{addr}'
        where
            e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""
        delete from emp
        where
            e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        
    def __str__(self):
        return "소리능력 " + str(self.flag_sound)
    
if __name__ == '__main__':
    de = DaoEmp()
    list = de.selectList()
    print(list)