#importamos de flask, la renderizacion de las template, flash (mostrar un mensaje que confirma que la aplicación recibió las credenciales), 
# redirect (redirigir al usuario a la página de índice de la aplicación.)
from flask import render_template, flash, redirect, url_for
#importamos de pps app
from pps import app
#importamos de forms.py la funcion LoginForm
from pps.forms import LoginForm
#usamos un decorator para la ruta /
@app.route('/')
#usamos un decorator para la ruta /index
@app.route('/index')
#definimos una funcion que se ejecuta al solicitar esta ruta
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)