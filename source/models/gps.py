import base64
import datetime
import string
import random
import json
import calendar

from flask import current_app as app
from flask import Flask, g, jsonify
from flask_security import UserMixin, RoleMixin

from sqlalchemy import desc
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, validates
from sqlalchemy import Boolean, DateTime, Column, Integer, Float, String, ForeignKey

from passlib.hash import pbkdf2_sha256
from itsdangerous import Serializer, JSONWebSignatureSerializer, BadSignature, BadData

from ..database.base import Base
from ..database.database import Session

class GPS(Base):
    __tablename__ = 'gps'
    id = Column(Integer(), primary_key=True)
    latitude = Column(Float())
    longitude = Column(Float())
    altitude = Column(Float())
    nauts = Column(Float())
    angle = Column(Float())
    satellites = Column(Integer())
    timestamp = Column(Integer())
    height = Column(Float())

    created = Column(DateTime(), default=datetime.datetime.utcnow)
    last_updated = Column(DateTime(), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def json(self):
        return {
        'type': 'gps',
        'id': self.id,
        'latitude': self.latitude,
        'longitude': self.longitude,
        'altitude': self.altitude,
        'nauts': self.nauts,
        'satellites': self.satellites,
        'angle': self.angle,
        'height': self.height,
        'timestamp': self.timestamp,
        'created': str(self.created),
        'last_updated': str(self.created)
         }
