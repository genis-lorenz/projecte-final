from flask import Blueprint, render_template
from wallacabanyes.db import get_db

bp = Blueprint('adlist', __name__)

@bp.route('/ads')
def adlist():
    db = get_db()

    ads = db.execute(
        'SELECT user.username as username, ad.name as name, ad.subjects as subjects, ad.price as price FROM ad LEFT JOIN user on ad.user_id  = user.id'
    ).fetchall()

    return render_template('adlist.html', ads=ads)