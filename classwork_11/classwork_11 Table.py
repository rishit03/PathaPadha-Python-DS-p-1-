import mysql.connector as mysql
con = mysql.connect(host="localhost",user="root",password="",db="newdb")
cur = con.cursor()
cur.execute("insert into student values(1,'Akash',82)")
con.commit()
