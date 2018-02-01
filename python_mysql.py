import pymysql
import pymysql.cursors


connection=pymysql.connect(host='localhost',
                           user='root',
                           password='237251',
                           db='user',
                           port=3306,
                           charset='utf8')
try:
    #获取一个游标
    with connection.cursor() as cursor:
        sql='select * from user'
        cout=cursor.execute(sql)
        print("数量："+str(cout))

        for row in cursor.fetchall():
            #注意int类型需要使用str函数转义
            print("ID:"+str(row[0])+'名字：'+row[1]+'性别：'+row[2])

        connection.commit()

finally:
    connection.close()
