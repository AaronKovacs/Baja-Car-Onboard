import json
import logging

from flask import Flask, g, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import event
import sqlalchemy.pool as Pool

from ..configuration.config import DB_URL
from .base import Base
from .query import BaseQuery

engine = create_engine(DB_URL(), convert_unicode=True)
db_session = None
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, query_cls=BaseQuery)