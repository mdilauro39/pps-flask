#importamos de pps login 
from pps import login
#importamos logica de hash
from werkzeug.security import generate_password_hash, check_password_hash
#importamos datetime
from datetime import datetime
#importamos de pps db
from pps import db
#importamos implementaciones genéricas para clases de modelos
from flask_login import UserMixin
#creamos una clase User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
#Verificacion de contraseña
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#clase de posteo
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
#Función de cargador de usuario de Flask-Login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))