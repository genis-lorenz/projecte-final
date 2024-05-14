from flask import Blueprint

bp = Blueprint('adlist', __name__)

@bp.route('/ads')
def adlist():
    return "Llistat d'anuncis"