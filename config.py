#importamos funcion para hacer oepraciones tipo bash
import os
basedir = os.path.abspath(os.path.dirname(__file__))
#defininimos una clase config tipo objeto
class Config(object):
    #variables de clase
    #clave criptográfica, útil para generar firmas o tokens.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #si ya esta creada la base de datos tomamos su posicion relativa y sino la creamos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False