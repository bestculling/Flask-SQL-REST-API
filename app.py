from flask import Flask
from models import db
from routes import tasks_bp

app = Flask(__name__)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(tasks_bp)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)