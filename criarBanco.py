from pinterestpython import database, app
from pinterestpython.models import Usuario, Foto

with app.app_context():
    database.create_all()   