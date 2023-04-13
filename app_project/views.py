from app_project import app, db, request
from app_project.models import Users

@app.route('/')
def default_connection():
    try:
        users = db.session.execute(db.select(Users).order_by(Users.id)).scalars()
        
        users_text = '<ul>'
        for user in users:
            users_text += '<li>' + str(user.id) + '. ' + user.login + '</li>'
        users_text += '</ul>'
        return users_text
    except Exception as e:

        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = Users(id = data['id'],
                             login = data['login'],
                             name = data['name'],
                             password = data['password'],
                             role = data['role'],
                             group_id = data['group_id'])
            
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"user {new_user.login} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
        
    elif request.method == 'GET':
        users = Users.query.all()
        results = [
            {
                "id": user.id,
                "login": user.login,
                "name": user.name,
                "password": user.password,
                "role": user.role,
                "group_id": user.group_id
            } for user in users]
        
        return {"count": len(results), "users": results}