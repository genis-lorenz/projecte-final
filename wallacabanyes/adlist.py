from flask import Blueprint, render_template
from wallacabanyes.db import get_db

bp = Blueprint('adlist', __name__)

@bp.route('/ads')
def adlist():
    db = get_db()

    ads = db.execute(
        'SELECT user.username as username, user.id as user_id, ad.name as name, ad.subjects as subjects, ad.price as price ' +
        'FROM ad ' + 
        'INNER JOIN user on ad.user_id  = user.id '
    ).fetchall()

    for ad in ads:
        img = db.execute(
            'SELECT * ' +
            'FROM img ' +
            'WHERE img.user_id = ?', str(ad['user_id'])
        ).fetchone()
        ad['img'] = img['filename']         

    return render_template('adlist.html', ads=ads)