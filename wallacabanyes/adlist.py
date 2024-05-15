from flask import Blueprint
from wallacabanyes.db import get_db

bp = Blueprint('adlist', __name__)

@bp.route('/ads')
def adlist():
    db = get_db()

    ads = db.execute(
        'SELECT * FROM ad'
    ).fetchall()

    return f"Llistat d'anuncis\nId: {ads[0]['id']} Name: {ads[0]['name']} Subjects: {ads[0]['subjects']} Price: {ads[0]['price']}"