from flask import Blueprint

bp = Blueprint('adcreate', __name__)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    return "Creació d'anunci"