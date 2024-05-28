from flask import Blueprint, send_from_directory

from .auth import login_required

bp = Blueprint('adimage', __name__)

@bp.route('/image/<path:filename>')
@login_required
def serve_image(filename):
    return send_from_directory('images', filename)