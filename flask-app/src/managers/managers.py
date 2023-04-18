from flask import Blueprint, request, jsonify, make_response
import json
from src import db


managers = Blueprint('managers', __name__)

# # Should return all call numbers associated with the employee id
# @managers.route('/employee/<employeeID>', methods=['GET'])
# def get_employee(employeeID):
#     cursor = db.get_db().cursor()
#     cursor.execute('SELECT * FROM Employees empl join Emergency emerg using emerg.Run')
#     row_headers = [x[0] for x in cursor.description]
#     json_data = []
#     theData = cursor.fetchall()
#     for row in theData:
#         json_data.append(dict(zip(row_headers, row)))
#     the_response = make_response(jsonify(json_data))
#     the_response.status_code = 200
#     the_response.mimetype = 'application/json'
#     return the_response

# testing
@managers.route('/test', methods=['GET'])
def test():
    cursor = db.get_db().cursor()
    cursor.execute("select * from Patient")
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    # return "hit this endpoint"
    return the_response

# get request for maintanence table datetimes based on call number
@managers.route('/maintenence/<callNum>', methods=['GET'])
def get_maintanence_datetimes(callNum):
    cursor = db.get_db().cursor()
    cursor.execute("select * from Patient")
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    # return "hit this endpoint"
    return the_response


# get request for maintanence table based on datetime
@managers.route('/maintanence/<datetime>', methods=['GET'])
def get_maintanence(datetime):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# get request for truck table based on call number
@managers.route('/truck/<callNum>', methods=['GET'])
def get_truck(callNum):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# get request for times table based on call number
@managers.route('/times/<callNum>', methods=['GET'])
def get_times(callNum):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



# get request for survey table ids based on call number
@managers.route('/surveys/<callNum>', methods=['GET'])
def get_survey_ids(callNum):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# get request for survey table based on survey ID
@managers.route('/surveys/<surveyID>', methods=['GET'])
def get_survey(surveyID):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# get request for patient table based on call number
@managers.route('/patient/<callNum>', methods=['GET'])
def get_patient(callNum):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# get request for shifts table based on call number
@managers.route('/shifts/<callNum>', methods=['GET'])
def get_shifts(callNum):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# get request for employees table based on call number
@managers.route('/employees/<callNum>', methods=['GET'])
def get_employee_ids(callNum):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# get request for employees table based on employee id
@managers.route('/employee/<employeeID>', methods=['GET'])
def get_employee(employeeID):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# get request for inventory table datetimes based on call number
@managers.route('/inventory/<callNum>', methods=['GET'])
def get_inventory_datetimes(callNum):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# get request for inventory table based on datetime
@managers.route('/inventory/<datetime>', methods=['GET'])
def get_inventory(datetime):
    cursor = db.get_db().cursor()
    cursor.execute('FILL IN')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


#############################
# Now for the put requests:
#############################



# patch request for truck table based on call number
@managers.route('/truck/<callNum>', methods=['PUT'])
def update_truck(callNum):
    updated_info = request.get_json()

    query = 'FILL IN'
    args = (updated_info['something'], 'and more ...')

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args) 
        return "truck updated successfully"
    except:
        return "Error in updating truck"
    


# patch request for times table based on call number
@managers.route('/times/<callNum>', methods=['PUT'])
def update_times_callNum(callNum):
    updated_info = request.get_json()

    query = 'FILL IN'
    args = (updated_info['something'], 'and more ...')

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args) 
        return "times updated successfully"
    except:
        return "Error in updating times"


# patch request for survey table based on call number
@managers.route('/survey/<datetime>', methods=['PUT'])
def update_times(datetime):
    updated_info = request.get_json()

    query = 'FILL IN'
    args = (updated_info['something'], 'and more ...')

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args) 
        return "times updated successfully"
    except:
        return "Error in updating times"
    


# patch request for patient table based on call number
@managers.route('/patient/<callNum>', methods=['PUT'])
def update_patient(callNum):
    updated_info = request.get_json()

    query = 'FILL IN'
    args = (updated_info['something'], 'and more ...')

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args) 
        return "times updated successfully"
    except:
        return "Error in updating times"
    



    


# patch request for employees table based on call number
@managers.route('/employees/<employeeID>', methods=['PUT'])
def update_employee(employeeID):
    updated_info = request.get_json()

    query = 'FILL IN'
    args = (updated_info['something'], 'and more ...')

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args) 
        return "times updated successfully"
    except:
        return "Error in updating times"
    


# patch request for maintanence table based on call number
@managers.route('/maintanence/<datetime>', methods=['PUT'])
def update_maintanence(datetime):
    updated_info = request.get_json()

    query = 'FILL IN'
    args = (updated_info['something'], 'and more ...')

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args) 
        return "times updated successfully"
    except:
        return "Error in updating times"



# patch request for shifts table based on call number