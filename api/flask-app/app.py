from flask import Flask, redirect, render_template, request, url_for
# from flask_mysqldb import MySQL
# import mysql.connector # type: ignore

app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'db'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'contato'
# my_sql = MySQL(app)
# Conexão com o banco de dados


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/academia")
def academia():
    return render_template('academia.html')

@app.route("/profissao")
def profissao():
    return render_template('profissao.html')

@app.route("/projetos")
def projetos():
    projetos = ['According with a internal client, our college team develop a complete stack in the agriculture field called Smart Farm', 'Developing a credit risk model with a complete stack (AWS + DB + FullStack)', 'Financial Feasibility Analysis Project in a Health Market (around R$ 25 mm/year)']
    return render_template('projetos.html', projetos=projetos)

@app.route("/tecnologias")
def tecnologias():
    return render_template('tecnologias.html')

@app.route("/links")
def links():
    return render_template('links.html')


# Rota para processar o formulário de cadastro
# @app.route('/links', methods=['POST'])
# def cadastrar():
#     print("Test!")
#     nome = request.form['nome']
#     sobrenome = request.form['sobrenome']
#     data_nasc = request.form['data_nasc']
#     endereco = request.form['endereco']
#     cidade = request.form['cidade']
#     estado = request.form['estado']
#     email = request.form['email']
#     db_config = mysql.connector.connect(
#         user= 'root',
#         password= 'root',
#         host= 'db',
#         database= 'contato'
#     )
#     print(db_config.is_connected())
#     print(nome, sobrenome, data_nasc, endereco, cidade, estado, email)
    
   

#     # Inserir os dados no banco de dados
#     sql = "INSERT INTO signup (nome, sobrenome, data_nasc, endereco, cidade, estado, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#     val = (nome, sobrenome, data_nasc, endereco, cidade, estado, email)
#     cursor = db_config.cursor()
#     cursor.execute(sql, val)
#     db_config.commit()
#     cursor.close()
    
    
#     # but a test
#     cur = my_sql.connection.cursor()
#     cur.execute("SELECT * FROM signup")
#     signup = cur.fetchall()
#     cur.close()
#     return render_template('links.html', signup=signup)
    
    
#     return redirect(url_for('links'))


# # Rota para exibir a lista de tarefas
# @app.route('/signup')
# def listar():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM signup")
    signup = cur.fetchall()
    cur.close()
    return render_template('links.html', signup=signup)

# Rota para detalhes projetos

if __name__ == "__main__":
    app.run(debug=True)


