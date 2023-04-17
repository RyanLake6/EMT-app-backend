from flask import Blueprint, request, jsonify, make_response
import json
from src import db


managers = Blueprint('managers', __name__)

# Get example
@managers.route('/manager', methods=['GET'])
def get_something():
    # fill in here
    return None