from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint('main', __name__)

@bp.route('/main')
@login_required
def main():
    return render_template('main.html')