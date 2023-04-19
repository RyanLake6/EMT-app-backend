from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


patients = Blueprint('patients', __name__)

# Get example
@patients.route('/patient/<MRN>', methods=['GET'])
def getPatientData(MRN):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Patient WHERE MRN = {0}'.format(MRN))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    cursor.close()

    return the_response


# Get example
@patients.route('/vitals/<MRN>', methods=['GET'])
def getPatientVitals(MRN):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Vitals WHERE MRN = {0}'.format(MRN))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    cursor.close()

    return the_response



# Get example
@patients.route('/medicine/<MRN>', methods=['GET'])
def getPatientMeds(MRN):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT medications FROM Medications WHERE MRN = {0}'.format(MRN))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    cursor.close()

    return the_response



# Get example
@patients.route('/allergies/<MRN>', methods=['GET'])
def getPatientAllergies(MRN):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Allergies FROM Allergies WHERE MRN = {0}'.format(MRN))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    cursor.close()

    return the_response



# Get example
@patients.route('/pmh/<MRN>', methods=['GET'])
def getPatientPMH(MRN):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT pastMedicalHistory FROM PastMedicalHistory WHERE MRN = {0}'.format(MRN))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    cursor.close()

    return the_response


# Get example
@patients.route('/runNumber/<runNumber>', methods=['GET'])
def getDataByRunNumber(runNumber):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Emergency.runNumber, Emergency.MRN, pt.firstName, pt.lastName, ee.employeeID FROM Emergency join Patient pt on Emergency.MRN = pt.MRN join EmergencyEmployee ee on Emergency.runNumber = ee.runNumber WHERE pt.runNumber = {0}'.format(runNumber))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    cursor.close()

    return the_response
