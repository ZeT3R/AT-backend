from app_project import app, db, request, render_template, form_json
from app_project.models import Users, Group_list, Event, Event_users, Tests
from app_project import cross_origin, func
from datetime import datetime


# --------------------DEFAULT ROUTE(MAIN PAGE)--------------------
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def default_connection(path):
    return render_template('index.html')


# --------------------GET ALL USERS AND POST ANY AMOUNT OF USERS IN DB--------------------
@app.route('/api/users', methods=['GET', 'POST'])
@cross_origin()
def handle_users():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = Users(login=data['login'],
                             name=data['name'],
                             password=data['password'],
                             role=data['role'],
                             group_id=data['group_id'])
            db.session.add(new_user)
            db.session.commit()

            cur_user = db.session.query(Users).filter(Users.login == data['login']).one()
            new_test = Tests(user_id=cur_user.id)
            db.session.add(new_test)
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
                                                                   "group_id": data['group_id']},
                                                                  synchronize_session='fetch')
    db.session.commit()
    return {"message": f"user {data['login']} has been updated successfully."}


@app.route('/api/full_user/<int:int_params>', methods=['GET'])
@cross_origin()
def handle_full_user(int_params):
    users = Users.query.filter(Users.id.like(int_params))
    groups = Group_list.query.filter(Group_list.id.like(users[0].group_id))
    tests = Tests.query.filter(Tests.user_id.like(int_params))

    results = {"user": {
        "id": users[0].id,
        "login": users[0].login,
        "name": users[0].name,
        "password": users[0].password,
        "role": users[0].role,
        "group_id": users[0].group_id
    }
    }

    results['group'] = {
        "group_id": groups[0].id,
        "name": groups[0].g_name
    }

    results['test'] = {}
    myList = []
    for test in tests:
        myList.append({"id": test.id, "test_name": test.test_name, "test_score": test.test_score})
    results['test'] = myList
    return results


@app.route('/api/users/delete/<int:int_params>', methods=['DELETE'])
@cross_origin()
def handle_users_delete(int_params):
    db.session.query(Users).filter(Users.id == int_params).delete(synchronize_session='fetch')
    db.session.commit()
    return {"message": f"user with id:{int_params} has been deleted successfully."}


# --------------------GET ALL EXISTING IN DB GROUPS OR ADD NEW ONES--------------------
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
                                                                             "g_name": data['name'], },
                                                                            synchronize_session='fetch')
    db.session.commit()
    return {"message": f"group {data['name']} has been updated successfully."}


@app.route('/api/grouplist/delete/<int:int_params>', methods=['DELETE'])
@cross_origin()
def handle_grouplist_delete(int_params):
    db.session.query(Group_list).filter(Group_list.id == int_params).delete(synchronize_session='fetch')
    db.session.commit()
    return {"message": f"group with id:{int_params} has been deleted successfully."}


@app.route('/api/time', methods=['GET'])
@cross_origin()
def handle_time():
    now = datetime.now()
    return (str(now))


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


@app.route("/api/tests", methods=['GET', 'POST', 'PUT'])
@cross_origin()
def handle_tests():
    if request.method == 'GET':
        tests = Tests.query.all()
        results = [
            {
                "id": test.id,
                "user_id": test.user_id,
                "test_name": test.test_name,
                "test_score": test.test_score
            } for test in tests]
        return {"count": len(results), "tests": results}

    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_test = Tests(user_id=data['user_id'],
                             test_name=data['test_name'],
                             test_score=data['test_score'])
            db.session.add(new_test)
            db.session.commit()
            return {"message": f"{new_test.user_id} users {new_test.test_name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'PUT':
        if request.is_json:
            data = request.get_json()
            db.session.query(Tests).filter(Tests.user_id.like(data["stud_id"]),
                                           Tests.test_name.like(data["test_name"])).update(
                {"test_score": data['test_score']}, synchronize_session='fetch')
            db.session.commit()
            return {"message": f"{data['stud_id']} users {data['name']} has been updated successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}


@app.route("/api/tests/<int:int_params>", methods=["DELETE"])
@cross_origin()
def handle_tests_delete(int_params):
    db.session.query(Tests).filter(Tests.id == int_params).delete(synchronize_session='fetch')
    db.session.commit()
    return {"message": f"test with id:{int_params} has been deleted successfully."}


start_json = "app_project/json_post/empty_json.json"


@app.route('/api/kr1', methods=['POST'])
@cross_origin()
def kr1():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json1(start_json, data)
    if (db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test1")).first() is None) == True:
        new_test = Tests(user_id=check_user_answers['stud_id'],
                         test_name='test1',
                         test_score=check_user_answers['score'])
        db.session.add(new_test)
        db.session.commit()
    else:
        db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test1")).update(
            {"test_score": check_user_answers['score']}, synchronize_session='fetch')
        db.session.commit()
    return {"right": right_answers, "checked": check_user_answers}


@app.route('/api/kr2', methods=['POST'])
@cross_origin()
def kr2():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json2(start_json, data)
    if (db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test2")).first() is None) == True:
        new_test = Tests(user_id=check_user_answers['stud_id'],
                         test_name='test2',
                         test_score=check_user_answers['score'])
        db.session.add(new_test)
        db.session.commit()
    else:
        db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test2")).update(
            {"test_score": check_user_answers['score']}, synchronize_session='fetch')
        db.session.commit()
    return {"right": right_answers, "checked": check_user_answers}


@app.route('/api/kr3', methods=['POST'])
@cross_origin()
def kr3():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json3(start_json, data)
    if (db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test3")).first() is None) == True:
        new_test = Tests(user_id=check_user_answers['stud_id'],
                         test_name='test3',
                         test_score=check_user_answers['score'])
        db.session.add(new_test)
        db.session.commit()
    else:
        db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test3")).update(
            {"test_score": check_user_answers['score']}, synchronize_session='fetch')
        db.session.commit()
    return {"right": right_answers, "checked": check_user_answers}


@app.route('/api/kr4', methods=['POST'])
@cross_origin()
def kr4():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json4(start_json, data)
    if (db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test4")).first() is None) == True:
        new_test = Tests(user_id=check_user_answers['stud_id'],
                         test_name='test4',
                         test_score=check_user_answers['score'])
        db.session.add(new_test)
        db.session.commit()
    else:
        db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test4")).update(
            {"test_score": check_user_answers['score']}, synchronize_session='fetch')
        db.session.commit()
    return {"right": right_answers, "checked": check_user_answers}


@app.route('/api/kr5', methods=['POST'])
@cross_origin()
def kr5():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json5(start_json, data)
    if (db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test5")).first() is None) == True:
        new_test = Tests(user_id=check_user_answers['stud_id'],
                         test_name='test5',
                         test_score=check_user_answers['score'])
        db.session.add(new_test)
        db.session.commit()
    else:
        db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test5")).update(
            {"test_score": check_user_answers['score']}, synchronize_session='fetch')
        db.session.commit()
    return {"right": right_answers, "checked": check_user_answers}


@app.route('/api/kr6', methods=['POST'])
@cross_origin()
def kr6():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json6(start_json, data)
    if (db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test6")).first() is None) == True:
        new_test = Tests(user_id=check_user_answers['stud_id'],
                         test_name='test6',
                         test_score=check_user_answers['score'])
        db.session.add(new_test)
        db.session.commit()
    else:
        db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test6")).update(
            {"test_score": check_user_answers['score']}, synchronize_session='fetch')
        db.session.commit()
    return {"right": right_answers, "checked": check_user_answers}


@app.route('/api/kr7', methods=['POST'])
@cross_origin()
def kr7():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json7(start_json, data)
    if (db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test7")).first() is None) == True:
        new_test = Tests(user_id=check_user_answers['stud_id'],
                         test_name='test7',
                         test_score=check_user_answers['score'])
        db.session.add(new_test)
        db.session.commit()
    else:
        db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test7")).update(
            {"test_score": check_user_answers['score']}, synchronize_session='fetch')
        db.session.commit()
    return {"right": right_answers, "checked": check_user_answers}


@app.route('/api/kr8', methods=['POST'])
@cross_origin()
def kr8():
    data = request.get_json()
    right_answers, check_user_answers = form_json.form_json8(start_json, data)
    if (db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test8")).first() is None) == True:
        new_test = Tests(user_id=check_user_answers['stud_id'],
                         test_name='test8',
                         test_score=check_user_answers['score'])
        db.session.add(new_test)
        db.session.commit()
    else:
        db.session.query(Tests).filter(Tests.user_id.like(check_user_answers["stud_id"]),
                                       Tests.test_name.like("test8")).update(
            {"test_score": check_user_answers['score']}, synchronize_session='fetch')
        db.session.commit()
    return {"right": right_answers, "checked": check_user_answers}


@app.route('/api/event', methods=['GET', 'POST', 'PUT'])
@cross_origin()
def handle_events():
    if request.method == 'GET':
        events = Event.query.all()
        events_users = Event_users.query.all()
        results = [
            {
                "id": event.id,
                "date": event.date,
                "length": event.length,
                "test_num": event.test_num,
                "description": event.description,
                "users": [{"id": e_user.id,
                           "user_id": e_user.user_id,
                           "event_id": e_user.event_id} for e_user in events_users if e_user.event_id == event.id]
            } for event in events]

        return results

    elif request.method == 'POST':
        data = request.get_json()
        new_event = Event(date=datetime.strptime(data['date'], "%a, %d %b %Y %H:%M:%S %Z"),
                          length=data['length'],
                          test_num=data['test_num'],
                          description=data['description'])
        db.session.add(new_event)
        db.session.commit()

        temp_max_id = db.session.query(func.max(Event.id)).scalar()
        last_event = Event.query.filter(Event.id.like(temp_max_id)).scalar()
        for d_user in data['users']:
            new_e_user = Event_users(user_id=d_user['user_id'],
                                     event_id=last_event.id)
            db.session.add(new_e_user)
            db.session.commit()
        return {"message": f"event {last_event.id} has been created successfully."}

    elif request.method == 'PUT':
        data = request.get_json()
        db.session.query(Event).filter(Event.id == data['id']).update(
            {"date": datetime.strptime(data['date'], "%a, %d %b %Y %H:%M:%S %Z"),
             "length": data['length'],
             "test_num": data['test_num'],
             "description": data['description']}, synchronize_session='fetch')
        db.session.commit()

        db.session.query(Event_users).filter(Event_users.event_id == data['id']).delete(synchronize_session='fetch')
        db.session.commit()

        for user in data['users']:
            new_e_user = Event_users(user_id=user['user_id'],
                                     event_id=data['id'])
            db.session.add(new_e_user)
            db.session.commit()
        return {"message": f"event {data['id']} has been updated successfully"}


@app.route('/api/event/<int:int_params>', methods=['GET', 'DELETE'])
@cross_origin()
def handle_spec_events(int_params):
    if request.method == 'GET':

        events = Event.query.filter(Event.id.like(int_params)).scalar()
        events_users = Event_users.query.filter(Event_users.event_id.like(events.id))

        results = {"event": {
            "id": events.id,
            "date": events.date,
            "length": events.length,
            "test_num": events.test_num,
            "description": events.description
        }
        }

        results['users'] = {}
        myList = []
        for e_user in events_users:
            myList.append({"id": e_user.id,
                           "user_id": e_user.user_id,
                           "event_id": e_user.event_id})
        results['users'] = myList
        return results

    elif request.method == 'DELETE':
        db.session.query(Event).filter(Event.id == int_params).delete(synchronize_session='fetch')
        db.session.commit()
        return {"message": f"event with id:{int_params} has been deleted successfully."}