from app_project import app, db, request, render_template, form_json
from app_project.models import Users, Group_list, Event
from app_project import cross_origin

#--------------------DEFAULT ROUTE(MAIN PAGE)--------------------
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def default_connection(path):
    return render_template('index.html')

#--------------------GET ALL USERS AND POST ANY AMOUNT OF USERS IN DB--------------------
@app.route('/api/users', methods=['GET', 'POST'])
@cross_origin()
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
    
@app.route('/api/users/update', methods=['PUT'])
@cross_origin()
def handle_users_update():
    data = request.get_json()
    db.session.query(Users).filter(Users.id == data['id']).update({"id": data['id'], 
                                                                   "login": data['login'], 
                                                                   "name": data['name'],
                                                                   "password": data['password'],
                                                                   "role": data['role'],
                                                                   "group_id": data['group_id']}, synchronize_session='fetch')
    db.session.commit()
    return {"message": f"user {data['login']} has been updated successfully."}

@app.route('/api/users/delete', methods=['DELETE'])
@cross_origin()
def handle_users_delete():
    data = request.get_json()
    db.session.query(Users).filter(Users.id == data['id']).delete(synchronize_session='fetch')
    db.session.commit()
    return {"message": f"user with id:{data['id']} has been deleted successfully."}

#--------------------GET ALL EXISTING IN DB GROUPS OR ADD NEW ONES--------------------
@app.route('/api/grouplist', methods=['GET', 'POST'])
@cross_origin()
def handle_grouplist():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_group = Group_list(g_name=data['name'])
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
                "name": group.g_name
            } for group in group_list]
        return {"count": len(results), "groups": results}
    
@app.route('/api/grouplist/update', methods=['PUT'])
@cross_origin()
def handle_grouplist_update():
    data = request.get_json()
    db.session.query(Group_list).filter(Group_list.id == data['id']).update({"id": data['id'], 
                                                                             "g_name": data['name'],}, synchronize_session='fetch')
    db.session.commit()
    return {"message": f"group {data['name']} has been updated successfully."}

@app.route('/api/grouplist/delete', methods=['DELETE'])
@cross_origin()
def handle_grouplist_delete():
    data = request.get_json()
    db.session.query(Group_list).filter(Group_list.id == data['id']).delete(synchronize_session='fetch')
    db.session.commit()
    return {"message": f"group with id:{data['id']} has been deleted successfully."}

##--------------------COMPARE POSTED USER WITH USERS THAT EXIST IN TABLE--------------------
@app.route('/api/user_compare', methods=['POST'])
@cross_origin()
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
@cross_origin()
def handler_g_ret(int_params):
        group_list = Group_list.query.all()
        for group in group_list:
            if int_params == group.id:
                results = {
                        "id": group.id,
                        "name": group.g_name
                    }
        return {"groups": results}



start_json = "app_project/json_post/empty_json.json"

@app.route('/api/kr1', methods=['POST'])
@cross_origin()
def kr1():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json1(start_json, data)
    return {"right": right_answers, "checked": check_user_answers}


@app.route('/api/kr3', methods=['POST'])
@cross_origin()
def kr3():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json3(start_json, data)
    return {"right": right_answers, "checked": check_user_answers}

@app.route('/api/kr4', methods=['POST'])
@cross_origin()
def kr4():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json4(start_json, data)
    return {"right": right_answers, "checked": check_user_answers}