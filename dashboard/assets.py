"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle
import os

# Ruta a la carpeta que contiene los archivos .less
less_folder = os.path.join(os.path.dirname(__file__), '../dashboard/', 'static', 'less')

# Obtener una lista de todos los archivos .less en la carpeta
less_files = [os.path.join(less_folder, f) for f in os.listdir(less_folder) if f.endswith('.less')]

def compile_static_assets(assets):
    """
    Compile stylesheets if in development mode.

    :param assets: Flask-Assets Environment
    :type assets: Environment
    """
    assets.auto_build = True
    assets.debug = True
    less_bundle = Bundle(
        *less_files,

        output="dist/css/styles.css",
        extra={"rel": "stylesheet/less"},
    )
    assets.register("less_all", less_bundle)
    if app.config["FLASK_ENV"] == "development":
        less_bundle.build()
    return assets
