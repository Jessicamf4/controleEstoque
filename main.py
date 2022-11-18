
import mysql.connector
from mysql.connector import Error

con = mysql.connector.connect(host='localhost', database='cadastro', user='jess', password='')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado!", db_info)

cursor = con.cursor()


recordsaffected = cursor.rowcount

cursor.close()
con.close()

## VALIDAÇÃO DE LOGIN



loginusuario = input("Você deseja: 1 - realizar cadastro , 2 - realizar login")
print("escolha" +loginusuario)

if loginusuario == "1":
    nomeCad = input("Digite seu nome:")
    emailCad = input("Digite seu email: ")
    senhaCad = input("Digite sua senha: ")
    dados = '\''+ nomeCad +'\'' + ',\''+ emailCad +'\','+ '\'' + senhaCad +'\'' + ')'
    print(dados)

    declaracao = """INSERT INTO pessoa 
    (nome, email, senha)
    VALUES ("""
    sql = declaracao + dados
    print(sql)
    try:
        con = mysql.connector.connect(host='localhost', database='cadastro', user='jess', password='')
    
        inserirCadastro = sql
        cursor = con.cursor()
        cursor.execute(inserirCadastro)
        con.commit()
        print(cursor.rowcount, "Registros inseridos na tabela!")
        cursor.close()
    except Error as erro:
        print("Falha ao inserir dados na tabela: { }".format(erro))


else:
    nomeLog = input("Digite seu nome: ")
    senhaLog = input("Digite sua senha: ")
    con = mysql.connector.connect(host='localhost', database='cadastro', user='jess', password='')
    try:
        cursor = con.cursor()
        cursor.execute("SELECT senha FROM cadastro.pessoa WHERE nome LIKE '{}'".format(nomeLog))   
        senha = cursor.fetchall()
        print(senha[0][0])
        cursor.close()
    except Error as erro:
        print("Erro {}".format(erro))
    if senhaLog == senha[0][0]:
        print("Sua senha está correta! Entrando...")
    else:
        print("Login e/ou senha incorretos..")


    



