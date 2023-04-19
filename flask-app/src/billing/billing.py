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


@billing.route('/billing/<runNumber>', methods=['POST'])
def add_card(runNumber):
    the_data = request.get_json()
    cost = the_data['cost']
    tax = the_data['tax']
    total = the_data['total']
    card_number = the_data['cardNumber']

    current_app.logger.info(the_data)

    cursor = db.get_db().cursor()
    query = "INSERT INTO Billing (cost, total, tax, runNumber, cardNumber) VALUES ('"
    query += cost + "', '" + total + "', '" + tax + "', '" + runNumber + "', '" + card_number + ")"

    current_app.logger.info(query)
    
    cursor.execute(query)
    db.get_db().commit()

    the_response = make_response('Success')
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response


@billing.route('/billing/<runNumber>', methods=['PUT'])
def update_card(runNumber):
    updated_info = request.get_json()

    query = '''
            UPDATE Billing
            SET cost = %s,
                total = %s,
                tax = %s,
                runNumber = %s,
                cardNumber = %s,
            WHERE runNumber = %s
    '''
    args = (updated_info['cost'], updated_info['total'], updated_info['tax'], runNumber, updated_info['cardNumber'], runNumber)

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args)
        return "Billing updated successfully"
    except:
        return "Error in updating Billing"


@billing.route('/billing/<runNumber>/<cardNumber>', methods=['DELETE'])
def delete_card(runNumber, cardNumber):
    query = 'DELETE FROM Billing WHERE runNumber = {0} AND cardNumber = {1}'.format(runNumber, cardNumber)

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query)
        return "billing updated successfully"
    except:
        return "Error in updating billing"
