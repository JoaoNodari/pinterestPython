# Criar fomulários do nosso site
from flask_wtf import FlaskForm # É a estrtura de formulário que vamos usar
from wtforms import StringField, PasswordField, SubmitField # Importa os campos de textos, números, etc...
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError # Importa os validadores dos campos
from pinterestpython.models import Usuario

class formLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botaoConfirmacao = SubmitField("Fazer Login")

class formCriarConta(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 13)])
    confirmacaoSenha =  PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botaoConfirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar.")