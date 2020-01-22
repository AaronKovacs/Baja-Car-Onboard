import datetime
import uuid
import os
import json

from flask import Flask, request, render_template, g, jsonify, Blueprint
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_restplus import Resource, Api, abort, fields
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from sqlalchemy import or_
from sqlalchemy import DateTime
from sqlalchemy import desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta


from source.helpers.helpers import BError
from source.views.local import api as local
from source.database.database import Session, engine
from source.database.base import Base

from source.models.gps import GPS

# Create all tables
Base.metadata.create_all(bind=engine)

# Create app
application = Flask(__name__)
application.config['DEBUG'] = False

api = Api(application)
api.add_namespace(local, path='/local')

@application.errorhandler(BError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return jsonify({ 'status_code' : 401 })

@api.errorhandler(BError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return { 'status_code' : 401 }