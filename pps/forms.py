#importamos la extension para representar formularios
from flask_wtf import FlaskForm
#importamos del paquete WTForms los campos necesarios
from wtforms import StringField, PasswordField, BooleanField, SubmitField
#importamo de wtforms el validador de campos
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')