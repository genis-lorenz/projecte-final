import functools
from flask import Blueprint, render_template, request, session, redirect, url_for, g
from wallacabanyes.db import get_db

bp = Blueprint('auth', __name__)

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
            return redirect(url_for('adcreate.create'))

        return render_template('error.html', error=error)

    return render_template('login.html')

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