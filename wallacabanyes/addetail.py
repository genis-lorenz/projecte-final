from flask import Blueprint
from markupsafe import escape

bp = Blueprint('addetail', __name__)

@bp.route('/ad/<id>')
def detail(id):
    return f"Detall de l'anunci amb id {escape(id)}"