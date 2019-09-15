import pymysql.cursors

#Connect to the database
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='1234',
                           db='test',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
print(connection)#address
print(type(connection))#<class 'pymysql.connections.Connection'>

try:
    
    with connection.cursor() as cursor:
        # create a new record
        sql="insert into users (email,password) values(%s,%s)"
        cursor.execute(sql,('webmaster@python.org', 'very-secret'))
    
    # connection is not autocommit by default. So you must commit to save
    # your changes
    #connection.commit()
    

    with connection.cursor() as cursor:
        # read a single record
        sql="select * from users where email=%s"
        cursor.execute(sql,('6755755@qq.com',))
        result=cursor.fetchone()
        print(result)
finally:
    connection.close()
