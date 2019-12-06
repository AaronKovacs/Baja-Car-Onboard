import json
import datetime
import uuid
import os
import threading
import extraction
import requests
import copy
import urllib

from flask import Flask, request, render_template, g, jsonify, Blueprint
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_restplus import Resource, Api, abort, Namespace

from sqlalchemy import or_
from sqlalchemy import DateTime
from sqlalchemy import desc
from sqlalchemy.sql.expression import func, select

from sqlakeyset import get_page, serialize_bookmark, unserialize_bookmark

from ..database.database import Session
from ..helpers.helpers import *
from ..helpers.namespace import APINamespace
from ..configuration.config import PAGE_SIZE, REMOTE

from ..models.gps import GPS

api = APINamespace('Local')

@api.route('/gps')
class GPS(Resource):
    def post(self):

        latitude = request.json.get('latitude', -1234)
        longitude = request.json.get('longitude', -1234)
        altitude = request.json.get('altitude', -1234)
        nauts = request.json.get('nauts', -1234)
        angle = request.json.get('angle', -1234)
        satellites = request.json.get('satellites', -1234)
        timestamp = request.json.get('timestamp', -1234)
        height = request.json.get('height', -1234)

        session = Session()

        last_location = session.query(GPS).filter_by(latitude=latitude, longitude=longitude).first()
        if last_location is None:
            gps = GPS(latitude=latitude, longitude=longitude, altitude=altitude, nauts=nauts, angle=angle, satellites=satellites, timestamp=timestamp, height=height)
            session.add(gps)
        else:
            last_location.timestamp = timestamp

        session.commit()
        session.close()

        data = {
        'latitude': latitude,
        'longitude': longitude,
        'altitude': altitude,
        'nauts': nauts,
        'angle': angle,
        'satellites': satellites,
        'timestamp': timestamp,
        'height': height
        }

        try:
            requests.post(REMOTE + '/car/upload', json=data)
        except:
            print("Couldn't POST GPS too remote.")

        return success()
