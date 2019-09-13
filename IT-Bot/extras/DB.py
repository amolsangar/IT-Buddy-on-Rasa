import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.197.194.145;'
                      'Database=WHDTESTDB;'
                      'uid=sa;'
                      'pwd=Pass-w0rd;'
                      )

cursor = conn.cursor()
cursor.execute('SELECT * FROM WHDTESTDB.dbo.CLIENT')

for row in cursor:
    print(row)