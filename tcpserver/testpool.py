import pymssql

from DBUtils.PooledDB import PooledDB

pool = PooledDB(creator=pymssql, mincached=1, maxcached=5,
                              host='10.25.18.9', user='sa', password='p@ssw0rd',
                              database='IVAS', charset='utf8', as_dict=True)

connection = pool.connection()

cursor = connection.cursor()
cursor.execute('select * from PUser')
result = cursor.fetchall()
#return to pool or destory
cursor.close()
connection.close()
print result
