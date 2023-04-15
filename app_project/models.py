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
    users = db.relationship("Users", backref=db.backref('group_list', uselist=False), lazy = 'dynamic')