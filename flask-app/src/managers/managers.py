from flask import Blueprint, request, jsonify, make_response
import json
from src import db


managers = Blueprint('managers', __name__)

# testing
@managers.route('/test', methods=['GET'])
def test():
    cursor = db.get_db().cursor()
    cursor.execute("select * from Shifts")
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

# Should return the employee id based of employee first and last name
@managers.route('/employees/<firstName>/<lastName>', methods=['GET'])
def get_employee(firstName, lastName):
    cursor = db.get_db().cursor()
    query = '''
          SELECT employeeID FROM Employees WHERE Employees.firstName=%s AND Employees.lastName=%s
            '''
    args = (firstName, lastName)
    cursor.execute(query, args)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Should return all run numbers associated with that employee
@managers.route('/runNumbers/<employeeID>', methods=['GET'])
def get_runNumbers(employeeID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Emergency.runNumber FROM Emergency join EmergencyEmployee using (runNumber) join Employees using (employeeID) where Employees.employeeID={0}'.format(employeeID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Should return all Truck info based on the run number
@managers.route('/Truck/<runNumber>', methods=['GET'])
def get_truck(runNumber):
    cursor = db.get_db().cursor()
    query = '''
          SELECT Truck.truckID, Truck.licensePlate, Truck.model FROM Truck join Emergency using(truckID) WHERE Emergency.runNumber=%s
            '''
    args = (runNumber)
    cursor.execute(query, args)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Should return all Times info based on the run number
@managers.route('/Times/<runNumber>', methods=['GET'])
def get_times(runNumber):
    cursor = db.get_db().cursor()
    query = '''
          SELECT * FROM Times join Emergency using(runNumber) WHERE Times.runNumber=%s
            '''
    args = (runNumber)
    cursor.execute(query, args)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Should return all Patient info based on the run number
@managers.route('/Patient/<runNumber>', methods=['GET'])
def get_patient(runNumber):
    cursor = db.get_db().cursor()
    query = '''
          SELECT Patient.firstName, Patient.lastName, Patient.dateOfBirth, Patient.MRN
          FROM Patient join Emergency using (runNumber) where Emergency.runNumber=%s
            '''
    args = (runNumber)
    cursor.execute(query, args)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Should return all Employee info based on the employee id
@managers.route('/Employee/<employeeID>', methods=['GET'])
def get_employee_info(employeeID):
    cursor = db.get_db().cursor()
    query = '''
          SELECT * FROM Employees where employeeID=%s
            '''
    args = (employeeID)
    cursor.execute(query, args)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


