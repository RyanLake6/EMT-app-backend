from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


patients = Blueprint('patients', __name__)

# Get example
@patients.route('/patient/<MRN>', methods=['GET'])
def update_insurance(MRN):
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


@patients.route('/patient/<MRN>/expenses', methods=['GET'])
def get_expenses(MRN):
    cursor = db.get_db().cursor()
    cursor.execute('')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    cursor.close()
    # return "hit this endpoint"
    return the_response


@patients.route('/patient/complaint', methods=['POST'])
def send_complaint(MRN):
    the_data = request.get_json()
    arg1 = the_data['']
    arg2 = the_data['']
    arg3 = the_data['']

    current_app.logger.info(the_data)

    cursor = db.get_db().cursor()
    query = "INSERT INTO products (product_name, description, category, list_price) VALUES ('"
    query += p_name + "', '" + p_desc + "', '" + p_category + "', " + str(p_price) + ")"

    current_app.logger.info(query)
    
    cursor.execute(query)
    db.get_db().commit()
    cursor.close()

    return "success!"
