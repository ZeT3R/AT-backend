from sqlalchemy.dialects.mysql import INTEGER
from app_project import db

#--------------------DECLARATION OF USERS TABLE MODEL--------------------
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(20))
    name = db.Column(db.String(40))
    password = db.Column(db.String(20))
    role = db.Column(db.Boolean, default=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group_list.id'))
    
#--------------------DECLARATION OF GROUP_LIST TABLE MODEL--------------------    
class Group_list(db.Model):
    __tablename__ = 'group_list'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(7))
    #users = db.relationship("Users", backref=db.backref('group_list', uselist=False), lazy = 'dynamic')
    
class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime)
    length = db.Column(INTEGER(unsigned=True))
    test_num = db.Column(db.Integer)
    test_status = db.Column(db.Integer)
    
class Event_groups(db.Model):
    __tablename__ = 'event_groups'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_id = db.Column(db.Integer)
    event_id = db.Column(db.Integer)
    
class Tests(db.Model):
    __tablename__= 'tests'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    test_name = db.Column(db.String(50))
    test_score = db.Column(db.Integer)
    