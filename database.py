import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='rk6239hx',
                             password='us10interstate39',
                             db='rk6239hx_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Search for a student
        searchName = input("Search for the name of the student: ")
        sql = "SELECT * FROM Students WHERE FirstName = " + "'" + searchName + "'"
                
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
