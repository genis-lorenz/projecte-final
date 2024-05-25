from flask import Blueprint, render_template
from markupsafe import escape
from wallacabanyes.db import get_db

bp = Blueprint('addetail', __name__)

@bp.route('/ad/<id>')
def detail(id):
    db = get_db()

    ad = db.execute(
        'SELECT user.username as username, ad.name as name, ad.description as description, ad.size as size, ad.subjects as subjects, ad.price as price ' + 
        'FROM ad LEFT JOIN user on ad.user_id  = user.id ' + 
        'WHERE ad.id = ?', id
    ).fetchone()

    return render_template('addetail.html', ad=ad)