from app_project import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20))
    name = db.Column(db.String(40))
    password = db.Column(db.String(20))
    role = db.Column(db.Boolean, default=False)
    group_id = db.Column(db.Integer)