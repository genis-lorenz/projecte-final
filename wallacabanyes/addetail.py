from flask import Blueprint, render_template
from markupsafe import escape
from wallacabanyes.db import get_db

bp = Blueprint('addetail', __name__)

@bp.route('/ad/<id>')
def detail(id):
    db = get_db()

    ad = db.execute(
        'SELECT user.username as username, ad.name as name, ad.description as description, ad.size as size, ad.subjects as subjects, ad.price as price, ad.contact as contact, img.filename as img ' + 
        'FROM ad ' + 
        'INNER JOIN user on ad.user_id  = user.id ' +
        'INNER JOIN img on ad.id = img.ad_id ' +
        'WHERE ad.id = ?', id
    ).fetchone()

    return render_template('addetail.html', ad=ad)