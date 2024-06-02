from flask import Blueprint, render_template, g
from wallacabanyes.db import get_db

from .auth import login_required

bp = Blueprint('adlist', __name__)

@bp.route('/ads')
@login_required
def adlist():
    db = get_db()
    grade = g.user['grade']

    ads = db.execute(
        'SELECT user.username as username, user.id as user_id, ad.name as name, ad.subjects as subjects, ad.price as price, img.filename as img, ad.id as adid, user.grade as grade ' +
        'FROM ad ' + 
        'INNER JOIN user on ad.user_id  = user.id ' +
        'INNER JOIN img on ad.id = img.ad_id ' +
        'WHERE user.grade = ?', (grade,)
    ).fetchall()

    return render_template('adlist.html', ads=ads)