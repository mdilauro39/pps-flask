#Este .py se usa declarar a un sub-directorio como un paquete y asi ser importado
#importamos flask.
from flask import Flask
#importamos de config.py la clase Config
from config import Config
#importamos sqlalquemy
from flask_sqlalchemy import SQLAlchemy
#importamos migracion
from flask_migrate import Migrate
#imnportamos Loginmanager
from flask_login import LoginManager
#creamos una instancia de Flask
app = Flask(__name__)
#importamos de config.py el objeto Config
app.config.from_object(Config)
#definimos Sqlalchemy 
db = SQLAlchemy(app)

migrate = Migrate(app, db)
#definimos instancia de Loginmanager
login = LoginManager(app)

from pps import routes, models
#importamos del sub-directorio pps routes.py

login = LoginManager(app)
login.login_view = 'login'
