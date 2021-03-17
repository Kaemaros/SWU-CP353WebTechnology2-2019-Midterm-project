from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()
class aboutusDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), unique=True, nullable=False)
    lastname = db.Column(db.String(50), unique=True, nullable=False)
    std_id = db.Column(db.String(12), unique=True, nullable=False)
    img_path = db.Column(db.String(120), unique=True, nullable=False)

