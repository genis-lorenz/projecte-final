from flask import Blueprint, send_from_directory

bp = Blueprint('adimage', __name__)

@bp.route('/image/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)