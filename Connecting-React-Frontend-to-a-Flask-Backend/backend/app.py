# Import the required libraries
from flask import Flask
from flask_cors import CORS


# Create various application instances
# Order matters: Initialize SQLAlchemy before Marshmallow
cors = CORS()


def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)

    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    cors.init_app(app)

    return app
