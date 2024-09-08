from flask import Flask
from models import db
from flask_login import LoginManager

DATABASE_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "lite_voyage"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}"

    
    db.init_app(app)

    from user.models import User
    from user.views import views
    app.register_blueprint(views, url_prefix="/views")

    
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
