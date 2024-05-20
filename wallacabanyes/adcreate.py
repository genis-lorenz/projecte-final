from flask import Blueprint, request, render_template
from wallacabanyes.db import get_db

bp = Blueprint('adcreate', __name__)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    user_id = 1
    cfgm = [ 'Hípica', 'Dinàmica', 'Itineraris', 'Muntanya', 'Bicicleta', 'Lleure', 'Natació', 'SOS', 'Aquàtic', 'Cordes']
    if request.method == 'GET':
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
    db.commit()

    return render_template('adcreate.html', subjects=cfgm)