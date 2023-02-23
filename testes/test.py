import mysql.connector

mydb = mysql.connector.connect(
  host="185.211.7.1",
     user="u266394849_teste",
  password="96891466Rr..",
  database="u266394849_testepython"
)

mycursor = mydb.cursor()

def inserir(wins, winssemg, winsg1, winsg2, brancos, seguidos, loss, atualizacao):
    sql = "INSERT INTO dados (wins, winssemg, winsg1, winsg2, brancos, seguidos, loss, atualizacao)VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (wins, winssemg, winsg1, winsg2, brancos, seguidos, loss, atualizacao)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")



inserir("100", "100", "100","100", "100", "100", "100", "2022-11-11")

