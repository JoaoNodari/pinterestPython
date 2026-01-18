# Criar as rotas do nosso site.
from flask import render_template, url_for, redirect
from pinterestpython import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from pinterestpython.forms import formLogin, formCriarConta
from pinterestpython.models import Usuario, Foto

@app.route("/", methods=["GET", "POST"])
def homepage():
    form_Login = formLogin()
    if form_Login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_Login.email.data).first()
        if usuario:
            bcrypt.check_password_hash(usuario.senha, form_Login.senha.data)
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template('html/homepage.html', form=form_Login)

@app.route("/criarconta", methods=["GET", "POST"])
def criarConta():
    form_CriarConta = formCriarConta()
    if form_CriarConta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_CriarConta.senha.data) # Para cripitografar a senha do usuário
        usuario = Usuario(username=form_CriarConta.username.data, senha=senha, email=form_CriarConta.email.data)
        #usuario = Usuario(username=form_CriarConta.username.data, email=form_CriarConta.email.data, senha=senha) # Colocando no banco de dados
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template('html/criarConta.html', form=form_CriarConta)

@app.route("/perfil/<id_usuario>")
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        # O usuario ta vendo o perfil dele
        return render_template("perfil.html", usuario=current_user)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('html/perfil.html', usuario=usuario)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))