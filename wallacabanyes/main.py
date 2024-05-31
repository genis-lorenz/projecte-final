from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint('main', __name__)

cfgm = [ 'Hípica', 'Dinàmica', 'Itineraris', 'Muntanya', 'Bicicleta', 'Lleure', 'Natació', 'SOS', 'Aquàtic', 'Cordes']

cfgs = [ 'Valoració', 'Dinàmica', 'Planificaió', 'Metodologia', 'Individuals', 'Lleure', 'Implements', "AFE d'equip", 'Turisme', 'Inclusió']

@bp.route('/main')
@login_required
def main():
    return render_template('main.html')