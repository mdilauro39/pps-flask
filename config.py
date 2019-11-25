#importamos funcion para hacer oepraciones tipo bash
import os
#defininimos una clase config tipo objeto
class Config(object):
    #variables de clase
    #clave criptográfica, útil para generar firmas o tokens.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'