from flask import Flask
from flask_cors import CORS
import os
from extensions import db

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:porkodi%405@localhost/assignment_portal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db.init_app(app)

from routes.assignment_routes import bp as assignment_bp
from routes.user_routes import bp as user_bp

app.register_blueprint(assignment_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)