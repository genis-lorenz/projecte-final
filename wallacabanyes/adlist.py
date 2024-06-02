from flask import Blueprint, render_template, g, request
from wallacabanyes.db import get_db

from .auth import login_required
from .main import cfgm, cfgs

bp = Blueprint('adlist', __name__)

@bp.route('/ads', methods=('GET', 'POST'))
@login_required
def adlist():
    db = get_db()
    grade = g.user['grade']
    if grade == 'CFGM':
        subjects = cfgm
    else:
        subjects = cfgs

    if request.method == 'GET':   
        ads = db.execute(
            'SELECT user.username as username, user.id as user_id, ad.name as name, ad.subjects as subjects, ad.price as price, img.filename as img, ad.id as adid, user.grade as grade ' +
            'FROM ad ' + 
            'INNER JOIN user on ad.user_id  = user.id ' +
            'INNER JOIN img on ad.id = img.ad_id ' +
            'WHERE user.grade = ?', (grade,)
        ).fetchall()
    else:
        filteredSubjects = request.form.getlist('subject_check')
        ads = db.execute(
            'SELECT user.username as username, user.id as user_id, ad.name as name, ad.subjects as subjects, ad.price as price, img.filename as img, ad.id as adid, user.grade as grade ' +
            'FROM ad ' + 
            'INNER JOIN user on ad.user_id  = user.id ' +
            'INNER JOIN img on ad.id = img.ad_id ' +
            'WHERE user.grade = ? AND instr(?, ad.subjects)', (grade, ','.join(filteredSubjects))
        ).fetchall()


    return render_template('adlist.html', ads=ads, subjects=subjects)