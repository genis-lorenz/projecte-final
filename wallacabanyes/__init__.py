from flask import Flask

def create_app():
    # create app
    app = Flask(__name__)

    from . import adcreate
    app.register_blueprint(adcreate.bp)

    from . import addetail
    app.register_blueprint(addetail.bp)

    from . import adlist
    app.register_blueprint(adlist.bp)

    return app