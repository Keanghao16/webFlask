from flask import Flask, render_template
# from flask_dance.contrib.google import make_google_blueprint, google

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ruppslayers69'

    from .views import views
    from .auth import auth
  

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app



