import mysql.connector

con = mysql.connector.connect(host='localhost', database='cadastro', user='jess', password='Je140404')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conctado!", db_info)

cursor = con.cursor()

# CREATE

sql = "INSERT INTO pessoa (nome, email, senha)  VALUES (%s, %s, %s) "

data = (
    "Jéssica",
    "jess@gmail.com",
    "abcd"
)

cursor.execute(sql, data)
con.commit()


#READ

sql = "SELECT * FROM pessoa"

cursor.execute(sql)
results = cursor.fetchall()

#função fetchall para recuperar todos os resultados da query SQL

for result in results:
    print(result)


#UPDATE

#sql = "UPDATE users SET name = %s, email = %s WHERE nome = %s"
#data = (
   # 'Jéssica Marques',
   # 'jesss@teste.com.br',
   # "Jéssica"
#)

#cursor.execute(sql, data)
#con.commit()

#recordsaffected = cursor.rowcount

#DELETE

#sql = "DELETE FROM users WHERE id = %s"
#data = (2,)

#cursor.execute(sql, data)
#con.commit()

recordsaffected = cursor.rowcount

cursor.close()
con.close()

print(data)
print(sql)
