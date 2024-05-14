import os

from flask import Flask

def create_app():
    # create app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'wallacabanyes.sqlite'),
    )

    # load the instance config, if it exists
    app.config.from_pyfile('config.py', silent=True)

     # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import adcreate
    app.register_blueprint(adcreate.bp)

    from . import addetail
    app.register_blueprint(addetail.bp)

    from . import adlist
    app.register_blueprint(adlist.bp)

    from . import db
    db.init_app(app)

    return app