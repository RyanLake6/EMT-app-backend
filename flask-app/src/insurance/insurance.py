from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


insurance = Blueprint('insurance', __name__)

@insurance.route('/provider/<MRN>', methods=['GET'])
def get_provider(MRN):
  cursor = db.get_db().cursor()
  cursor.execute('SELECT provider FROM Insurance WHERE MRN = {0}'.format(MRN))
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
@insurance.route('/insurance/<MRN>', methods=['GET'])
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


@insurance.route('/insurance/<MRN>', methods=['POST'])
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


@insurance.route('/insurance/<MRN>', methods=['PUT'])
def update_insurance(MRN):
  the_data = request.get_json()
  subscriber_id = the_data['subscriberID']
  group_number = the_data['groupNumber']
  provider = the_data['provider']
  subscriber_dob = the_data['subscriberDateOfBirth']
  subscriber_first = the_data['firstNameSubscriber']
  subscriber_last = the_data['lastNameSubscriber']

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
      return "Insurance updated successfully"
  except:
      return "Error in updating Insurance"


@insurance.route('/insurance/<MRN>', methods=['DELETE'])
def delete_insurance(MRN):
  updated_info = request.get_json()

  query = 'DELETE FROM Insurance WHERE MRN = %s AND provider = %s AND subscriberID = %s'
  args = (MRN, updated_info['provider'], updated_info['subscriberID'])

  cursor = db.get_db().cursor()
  try:
      cursor.execute(query, args) 
      return "Insurance deleted successfully"
  except:
      return "Error in deleting insurance"
  