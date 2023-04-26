# Projeto Controle de estoque

Início de um projeto de um controle de estoque. Este projeto realiza as principais funções de um CRUD (Create, Read, Update, Delete) utilizando a linguagem Python e o banco de dados MySQL.

A seguir é possível ver as principais funções:


##Create

sql = "INSERT INTO pessoa (nome, email, senha)  VALUES (%s, %s, %s) "

data = (
    "Jéssica",
    "jess@gmail.com",
    "abcd"
)

cursor.execute(sql, data)
con.commit()


##READ

sql = "SELECT * FROM pessoa"

cursor.execute(sql)
results = cursor.fetchall()

#função fetchall para recuperar todos os resultados da query SQL

for result in results:
    print(result)


##UPDATE

sql = "UPDATE users SET name = %s, email = %s WHERE nome = %s"
data = (
    'Jéssica Marques',
    'jesss@teste.com.br',
    "Jéssica"
)

cursor.execute(sql, data)
con.commit()

recordsaffected = cursor.rowcount

##DELETE

sql = "DELETE FROM users WHERE id = %s"
data = (2,)

cursor.execute(sql, data)
con.commit()


## INSERIR UM USUÁRIO

def insert_user(nome,email, senha):
    try:
        cursor = self.connection.cursor()
        cursor.execute("""

            INSERT INTO pessoa(nome, email, senha) VALUES (?, ?, ?)

        """(nome, email, senha))
        self.connection.commit()

    except AttributeError:
        print("faça a conexão")


## VALIDAÇÃO DE LOGIN

def check_user(email,senha):
    try:
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM pessoa;
        """)

        for linha in cursor.fetchall():
            if linha[2].upper() == email.upper() and linha[3]== senha:
                return "Usuario"
                break
            else:
                continue
        return "Sem acesso"
    except:
        pass
