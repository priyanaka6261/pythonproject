from mysql.connector import *
con=connect(host="localhost",user="root",password="",database="database")
cur=con.cursor()
rollno=int(input("enter your roll no"))
name=input("enter your name")
#query=f" Insert into student(rollno,name) values ({rollno},'{name}')"
#t=cur.execute(query)
# another way  to write this query
query="Insert into student(rollno,name) values(%s,%s)"
val=(rollno,name)
cur.execute(query,val)

con.commit()
print( cur.rowcount,"record inserted")
con.close()
