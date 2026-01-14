# Criar fomulários do nosso site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class formLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botaoConfirmacao = SubmitField("Fazer Login")


class formCriarConta(FlaskForm):
    username = StringField("E-mail", validators=[DataRequired(), Email()])
    email = 
    senha = 
    confirmacaoSenha = 
    botaoConfirmacao = 