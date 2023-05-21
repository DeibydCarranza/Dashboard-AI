"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment


def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our core Flask app       
        from . import routes
        from .assets import compile_static_assets

        # Import Dash application
        from .algorithms.apriori import init_dashboard_apriori
        from .algorithms.clustering import init_dashboard_cluster
        from .algorithms.metrics import init_dashboard_metrics

        app = init_dashboard_apriori(app)
        app = init_dashboard_cluster(app)
        app = init_dashboard_metrics(app)

        # Compile static assets
        compile_static_assets(assets)

        return app
