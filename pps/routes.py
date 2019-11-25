#importamos de flask, la renderizacion de las template, flash (mostrar un mensaje que confirma que la aplicación recibió las credenciales), 
# redirect (redirigir al usuario a la página de índice de la aplicación.)
from flask import render_template, flash, redirect, url_for
#importamos de pps app
from pps import app
#importamos de forms.py la funcion LoginForm
#lógica de función de vista de inicio de sesión
from pps.forms import LoginForm
from flask_login import current_user, login_user
from pps.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
#usamos un decorator para la ruta /
@app.route('/')
#usamos un decorator para la ruta /index
@app.route('/index')
#definimos una funcion que se ejecuta al solicitar esta ruta
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    #devuelve una renderizacion de la pagina index.html y por parametro
    #un titulo, usuario y una lista con 2 diccionarios
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))