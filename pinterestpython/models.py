# Criar estrutura do banco de dados
from pinterestpython import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario): # FUNÇÃO OBRIGATORIA PARA ESTRUTURA DO LOGIN
    return Usuario.query.get(int(id.usuario)) # Para buscar informação no banco

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref='usuario', lazy=True)

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    dataCriacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    idUsuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)