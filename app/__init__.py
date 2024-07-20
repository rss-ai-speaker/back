import os

from flask import Flask

import config
from . import apis
from .database import db, migrate


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()

    if test_config is None:
        app.config.from_object(config)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # register bp
    app.register_blueprint(apis.bp)

    return app
