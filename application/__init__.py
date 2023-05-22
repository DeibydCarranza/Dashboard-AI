from flask import Flask, render_template
from flask_assets import Environment

app = Flask(__name__, instance_relative_config=False)
app.config.from_object("config.Config")
assets = Environment()
assets.init_app(app)

with app.app_context():
    # Import parts of our core Flask app       
    from . import routes
    from .assets import compile_static_assets

    # # Import Dash application
    # from .algorithms.apriori import init_dashboard_apriori

    # app = init_dashboard_apriori(app)
    # Compile static assets
    compile_static_assets(assets)