from app_project import app, db, request, render_template, ltj
from app_project.models import Users, Group_list, Event

#--------------------DEFAULT ROUTE(MAIN PAGE)--------------------
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def default_connection(path):
    return render_template('index.html')

#--------------------GET ALL USERS AND POST ANY AMOUNT OF USERS IN DB--------------------
@app.route('/api/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = Users(login = data['login'],
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

#--------------------GET ALL EXISTING IN DB GROUPS OR ADD NEW ONES--------------------
@app.route('/api/grouplist', methods=['GET', 'POST'])
def handle_grouplist():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_group = Group_list(g_name=data['g_name'])
            db.session.add(new_group)
            db.session.commit()
            return {"message": f"group {new_group.g_name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
        
    elif request.method == 'GET':
        group_list = Group_list.query.all()
        results = [
            {
                "id": group.id,
                "g_name": group.g_name
            } for group in group_list]
        return {"count": len(results), "groups": results}

##--------------------COMPARE POSTED USER WITH USERS THAT EXIST IN TABLE--------------------
@app.route('/api/user_compare', methods=['POST'])
def handler_usercomp():
    if request.is_json:
        data = request.get_json()
        current_user = Users(login=data['login'],
                             password=data['password'])
        users = Users.query.all()
        for user in users:
            if current_user.login == user.login and current_user.password == user.password:
               result = {
                "id": user.id,
                "login": user.login,
                "name": user.name,
                "password": user.password,
                "role": user.role,
                "group_id": user.group_id
               }
               return {"user": result}
        return {"error": "Login or password incorrect"} 
    
@app.route('/api/g_ret/<int:int_params>', methods=['GET'])
def handler_g_ret(int_params):
        group_list = Group_list.query.all()
        for group in group_list:
            if int_params == group.id:
                results = {
                        "id": group.id,
                        "g_name": group.g_name
                    }
        return {"groups": results}
    
@app.route('/api/kr2', methods=['POST'])
def kr2():
    data = request.get_json()
    ltj.clear_json("app_project/_2kr/KR2_json.json")
    right_answers, check_user_answers = ltj._2KR_load_to_json("app_project/_2kr/KR2_json.json", data)
    return {"right": right_answers, "checked": check_user_answers}
    
    #"app_project/_2kr/test_front_json.json"
    
@app.route("/api/events/", methods=["POST"])
def handler_events():
    events = Event.query.all()