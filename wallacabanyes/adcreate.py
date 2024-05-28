import os
from flask import Blueprint, request, render_template
from werkzeug.utils import secure_filename
from wallacabanyes.db import get_db

bp = Blueprint('adcreate', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = "images"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/create', methods=('GET', 'POST'))
def create():
    user_id = 1
    cfgm = [ 'Hípica', 'Dinàmica', 'Itineraris', 'Muntanya', 'Bicicleta', 'Lleure', 'Natació', 'SOS', 'Aquàtic', 'Cordes']
    if request.method == 'GET':
        return render_template('adcreate.html', subjects=cfgm)
    
    name = request.form['name']
    contacte = request.form['contacte']
    description = request.form['description']
    size = request.form['size']
    price = request.form['price']
    subjects = request.form.getlist('subject_check')

    if not subjects:
        return render_template('error.html', error='No has seleccionat matèria')
    
    if 'file' not in request.files:
        return render_template('error.html', error='No has seleccionat imatges')
    
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return render_template('error.html', error='No has seleccionat imatges o tipus de fitxer no permés')

    filename = secure_filename(file.filename)
    userfilename = str(user_id) + '-' + filename
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, UPLOAD_FOLDER, userfilename)
    file.save(path)

    db = get_db()
    cursor = db.execute(
        "INSERT INTO ad (user_id, contact, name, description, size, price, subjects) " +  
        "VALUES (?, ?, ?, ?, ?, ?, ?) " +
        "RETURNING *;",
        (user_id, contacte, name, description, size, price, ','.join(subjects)),
    )
    ad = cursor.fetchone()

    db.execute(
        "INSERT INTO img (ad_id, filename) VALUES (?, ?)",
        (ad['id'], userfilename)
    )
    db.commit()

    return render_template('adcreate.html', subjects=cfgm)