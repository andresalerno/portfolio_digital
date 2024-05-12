from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('projetos.html')

@app.route("/tecnologias")
def tecnologias():
    return render_template('tecnologias.html')

@app.route("/links")
def links():
    return render_template('links.html')