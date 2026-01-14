# Criar as rotas do nosso site.
from flask import render_template, url_for
from pinterestpython import app
from flask_login import login_required

@app.route("/")
def homepage():
    return render_template('html/homepage.html')

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template('html/perfil.html', usuario=usuario)