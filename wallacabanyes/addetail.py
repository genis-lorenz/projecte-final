from flask import Blueprint
from markupsafe import escape
from wallacabanyes.db import get_db

bp = Blueprint('addetail', __name__)

@bp.route('/ad/<id>')
def detail(id):
    db = get_db()

    ad = db.execute(
        'SELECT * FROM ad WHERE id = ?', id
    ).fetchone()

    return f"Detall de l'anunci amb id {escape(id)}\nName: {ad['name']} Subjects: {ad['subjects']} Price: {ad['price']}"