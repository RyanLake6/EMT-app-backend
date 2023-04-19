from flask import Blueprint, request, jsonify, make_response
import json
from src import db


insurance = Blueprint('insurance', __name__)

# Get example
@insurance.route('/insurance/<MRN>', methods=['GET'])
def get_insurance(MRN):
  cursor = db.get_db().cursor()
  cursor.execute('SELECT * FROM Insurance WHERE MRN EQUALS {0}'.format(MRN))
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


@insurance.route('/insurance/<MRN>', methods=['POST'])
def add_insurance():
  the_data = request.get_json()
  subscriber_id = the_data['subscriberID']
  group_number = the_data['groupNumber']
  provider = the_data['provider']
  subscriber_dob = the_data['subscriberDateOfBirth']
  subscriber_first = the_data['firstNameSubscriber']
  subscriber_last = the_data['lastNameSubscriber']

  query = '''
          INSERT INTO Insurance (subscriberID, groupNumber, provider, subscriberDateOfBirth, firstNameSubscriber, lastNameSubscriber) 
          VALUES ({0}, {1}, {2}, {3}, {4}, {5})
  '''.format(subscriber_id, group_number, provider, subscriber_dob, subscriber_first, subscriber_last)
  
  cursor = db.get_db().cursor()
  cursor.execute(query)
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
          WHERE MRN EQUALS %s
  '''
  args = (subscriber_id, group_number, provider, subscriber_dob, subscriber_first, subscriber_last, MRN)

  cursor = db.get_db().cursor()
  try:
      cursor.execute(query, args) 
      return "Insurance updated successfully"
  except:
      return "Error in updating Insurance"


@insurance.route('/insurance/<MRN>', methods=['DELETE'])
def delete_insurance():
  updated_info = request.get_json()

  query = 'DELETE FROM Insurance WHERE provider = %s AND subscriberID = %s'
  args = (updated_info['provider'], updated_info['subscriberID'])

  cursor = db.get_db().cursor()
  try:
      cursor.execute(query, args) 
      return "Insurance updated successfully"
  except:
      return "Error in updating insurance"
  