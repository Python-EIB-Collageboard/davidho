from flask import Flask

def create_app():
    app = Flask(__name__)
    from .products.routes import products_bp
    app.register_blueprint(products_bp)
    return app