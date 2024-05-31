import re
import functools
from flask import Blueprint, render_template, request, session, redirect, url_for, g
from wallacabanyes.db import get_db

bp = Blueprint('auth', __name__)

regex = r'\b[A-Za-z0-9._%+-]+@alumnat\.institutcabanyes\.cat\b'

@bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Usuari no vàlid'
        elif not user['password'] == password:
            error = 'Contrasenya incorrecta'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('main.main'))

        return render_template('error.html', error=error)

    return render_template('login.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        grade = request.form['grade']
        db = get_db()
        error = None

        if not username:
            error = 'Correu requerit'
        elif not password:
            error = 'Contrasenya requerida'
        elif password != password2:
            error = 'Les contrasenyes no coincideixen'
        elif not (re.fullmatch(regex, username)):
            error = 'Correu Invàlid'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password, grade) VALUES (?, ?, ?)",
                    (username, password, grade)
                ),
                db.commit()
            except db.IntegrityError:
                error = f"Usuari {username} ja registrat."
            else:
                return redirect(url_for("auth.login"))

        return render_template('error.html', error=error)

    return render_template('register.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view       