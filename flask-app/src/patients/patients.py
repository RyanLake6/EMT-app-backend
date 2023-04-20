from flask import Blueprint, request, jsonify, make_response, current_app
import json
from datetime import datetime
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
    cursor.execute('SELECT e.firstName, e.lastName, ee.employeeID FROM Emergency join Patient pt on Emergency.MRN = pt.MRN join EmergencyEmployee ee on Emergency.runNumber = ee.runNumber join Employees e on ee.employeeID = e.employeeID WHERE pt.runNumber = {0}'.format(runNumber))
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


#####################################################
#NEEDS TO BE WRITTEN
#####################################################
@patients.route('/patient/<MRN>/complaint', methods=['POST'])
def send_complaint(MRN):
    the_data = request.get_json()
    rating = the_data['rating']
    response = the_data['response']

    current_app.logger.info(the_data)

    cursor = db.get_db().cursor()
    query = "INSERT INTO Survey (rating, response, MRN) VALUES (%s, %s, %s)"
    args = (rating, response, MRN)

    current_app.logger.info(query)
    
    cursor.execute(query, args)
    db.get_db().commit()
    cursor.close()

    return "success!"

# -------------------------- BILLING --------------------------

@patients.route('/billing/<runNumber>', methods=['GET'])
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

@patients.route('/cc/<cardNumber>', methods=['GET'])
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


# @patients.route('/billing/<runNumber>/<cardNumber>', methods=['POST'])
# def add_card():
#     the_data = request.get_json()
#     cost = the_data['cost']
#     tax = the_data['tax']
#     total = the_data['total']
#     run_number = the_data['runNumber']
#     card_number = the_data['cardNumber']

#     current_app.logger.info(the_data)

#     cursor = db.get_db().cursor()
#     query = "INSERT INTO Billing (cost, total, tax, runNumber, cardNumber) VALUES ('"
#     query += cost + "', '" + total + "', '" + tax + "', '" + run_number + "', '" + card_number + ")"

#     current_app.logger.info(query)
    
#     cursor.execute(query)
#     db.get_db().commit()

#     the_response = make_response('Success')
#     the_response.status_code = 200
#     the_response.mimetype = 'application/json'

#     # return "hit this endpoint"
#     return the_response


#####################################################
#NEEDS TO BE WRITTEN
#####################################################
@patients.route('/billing/update', methods=['PATCH'])
def update_card():
    updated_info = request.get_json()

    query = '''
            SET foreign_key_checks = 0; 
            UPDATE PaymentInfo
            SET cardNumber = %s,
            WHERE cardNumber = %s; 

            UPDATE Billing
            SET cardNumber = %s,
            WHERE cardNumber = %s; 
            SET foreign_key_checks = 1;
    '''

    current_app.logger.info(query)
    args = (int(updated_info['newCard']), int(updated_info['currentCard']), int(updated_info['newCard']), int(updated_info['currentCard']))

    current_app.logger.info(args)

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, args)
        return "Billing updated successfully"
    except:
        response = make_response("<h1>Unable to update billing info</h1>")
        response.status_code = 500
        return response


#####################################################
#NEEDS TO BE WRITTEN
#####################################################
@patients.route('/billing/<runNumber>', methods=['PUT'])
def pay_bill(runNumber):
    updated_info = request.get_json()
    cursor = db.get_db().cursor()

    cursor.execute('SELECT Total FROM Billing WHERE runNumber = {0}'.format(runNumber))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = json.loads(jsonify(json_data).data.decode('utf-8').replace("'", '"'))

    current_app.logger.info(the_response)

    # update with new total
    query = '''
            UPDATE Billing SET Total = %s WHERE runNumber = %s
    '''
    args = (the_response[0]['Total'] - float(updated_info['amount']), runNumber,)

    try:
        cursor.execute(query, args)
        db.get_db().commit()
        cursor.close()
        return "billing updated successfully"
    except:
        return "Error in updating billing"
    


@patients.route('/billing/<runNumber>/<cardNumber>', methods=['DELETE'])
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

# -------------------------- INSURANCE --------------------------

@patients.route('/provider/<MRN>', methods=['GET'])
def get_provider(MRN):
  cursor = db.get_db().cursor()
  cursor.execute('SELECT provider, MRN FROM Insurance WHERE MRN = {0}'.format(MRN))
  row_headers = [x[0] for x in cursor.description]
  json_data = []
  theData = cursor.fetchall()
  for row in theData:
      json_data.append(dict(zip(row_headers, row)))
  the_response = make_response(jsonify(json_data))
  the_response.status_code = 200
  the_response.mimetype = 'application/json'
  
  return the_response

# Get example
@patients.route('/insurance/<MRN>', methods=['GET'])
def get_insurance(MRN):
  the_data = request.get_json()
  cursor = db.get_db().cursor()

  query = 'SELECT subscriberID, groupNumber, subscriberDateOfBirth, firstNameSubscriber, lastNameSubscriber FROM Insurance WHERE MRN = %s AND provider = %s'

  args = (MRN, the_data['provider'])

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


@patients.route('/insurance/<MRN>', methods=['POST'])
def add_insurance(MRN):
  the_data = request.get_json()
  subscriber_id = the_data['subscriberID']
  group_number = the_data['groupNumber']
  provider = the_data['provider']
  subscriber_dob = the_data['subscriberDateOfBirth']
  subscriber_first = the_data['firstNameSubscriber']
  subscriber_last = the_data['lastNameSubscriber']

  query = '''
          INSERT INTO Insurance (subscriberID, groupNumber, provider, subscriberDateOfBirth, firstNameSubscriber, lastNameSubscriber, MRN)
          VALUES (%s, %s, %s, %s, %s, %s, %s)
  '''
  args = (subscriber_id, group_number, provider, subscriber_dob, subscriber_first, subscriber_last, MRN)
  
  cursor = db.get_db().cursor()

  current_app.logger.info(args)

  cursor.execute(query, args)
  db.get_db().commit()

  the_response = make_response('Success')
  the_response.status_code = 200
  the_response.mimetype = 'application/json'

  return the_response


@patients.route('/insurance/<MRN>', methods=['PUT'])
def update_insurance(MRN):
  the_data = request.get_json()
  subscriber_id = the_data['subscriberID']
  group_number = the_data['groupNumber']
  provider = the_data['provider']
  subscriber_dob = the_data['subscriberDateOfBirth']
  subscriber_first = the_data['firstNameSubscriber']
  subscriber_last = the_data['lastNameSubscriber']

    #Sun, 11 Nov 1962 00:00:00 GMT
  subscriber_dob = datetime.strptime(subscriber_dob, '%a, %d %b %Y %H:%M:%S %Z').date()

  query = '''
          UPDATE Insurance
          SET subscriberID = %s,
              groupNumber = %s,
              provider = %s,
              subscriberDateOfBirth = %s,
              firstNameSubscriber = %s,
              lastNameSubscriber = %s
          WHERE MRN = %s
  '''
  args = (subscriber_id, group_number, provider, subscriber_dob, subscriber_first, subscriber_last, MRN)

  cursor = db.get_db().cursor()
  try:
      cursor.execute(query, args)
      db.get_db().commit()
      return "Insurance updated successfully"
  except:
      return "Error in updating Insurance"


@patients.route('/insurance/<MRN>', methods=['DELETE'])
def delete_insurance(MRN):
  updated_info = request.get_json()

  query = 'DELETE FROM Insurance WHERE MRN = %s AND provider = %s AND subscriberID = %s'
  args = (MRN, updated_info['provider'], updated_info['subscriberID'])

  cursor = db.get_db().cursor()
  try:
      cursor.execute(query, args) 
      db.get_db().commit()
      return "Insurance deleted successfully"
  except:
      return "Error in deleting insurance"