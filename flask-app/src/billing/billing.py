from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


billing = Blueprint('billing', __name__)


@billing.route('/billing/<runNumber>', methods=['GET'])
def get_billing(runNumber):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Billing WHERE runNumber = {0}'.format(runNumber))
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

@billing.route('/cc/<cardNumber>', methods=['GET'])
def get_cc(cardNumber):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM PaymentInfo WHERE cardNumber = {0}'.format(cardNumber))
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


@billing.route('/billing/<runNumber>/<cardNumber>', methods=['POST'])
def add_card():
    the_data = request.get_json()
    cost = the_data['cost']
    tax = the_data['tax']
    total = the_data['total']
    run_number = the_data['runNumber']
    card_number = the_data['cardNumber']

    current_app.logger.info(the_data)

    cursor = db.get_db().cursor()
    query = "INSERT INTO Billing (cost, total, tax, runNumber, cardNumber) VALUES ('"
    query += cost + "', '" + total + "', '" + tax + "', '" + run_number + "', '" + card_number + ")"

    current_app.logger.info(query)
    
    cursor.execute(query)
    db.get_db().commit()

    the_response = make_response('Success')
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    # return "hit this endpoint"
    return the_response


@billing.route('/billing/<CurrentCardNumber>/<NewCardNumber>', methods=['PUT'])
def update_card():
    updated_info = request.get_json()

    query = '''
            
    '''
    args = (updated_info['something'], 'and more ...')

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args) 
        return "billing updated successfully"
    except:
        return "Error in updating billing"


@billing.route('/billing/<runNumber>/<cardNumber>', methods=['DELETE'])
def delete_card():
    updated_info = request.get_json()

    query = 'FILL IN'
    args = (updated_info['something'], 'and more ...')

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args) 
        return "billing updated successfully"
    except:
        return "Error in updating billing"
