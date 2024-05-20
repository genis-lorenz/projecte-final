from flask import Blueprint, request, render_template, flash
from wallacabanyes.db import get_db

bp = Blueprint('adcreate', __name__)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    user_id = 1
    if request.method == 'GET':
        cfgm = [ 'Hípica', 'Dinàmica', 'Itineraris', 'Muntanya', 'Bicicleta', 'Lleure', 'Natació', 'SOS', 'Aquàtic', 'Cordes']
        return render_template('adcreate.html', subjects=cfgm)
    
    name = request.form['name']
    description = request.form['description']
    size = request.form['size']
    price = request.form['price']
    subjects = request.form.getlist('subject_check')

    if not subjects:
        return render_template('error.html', error='No has seleccionat matèria')
    
    db = get_db()
    db.execute(
        "INSERT INTO ad (user_id, name, description, size, price, subjects) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, name, description, size, price, ','.join(subjects)),
    )

    return render_template('adlist.html')