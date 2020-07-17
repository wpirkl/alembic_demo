import os

import json

import uuid

import logging

from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects import mysql, sqlite
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql.expression import false, true

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import Numeric
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import UnicodeText

from sqlalchemy.orm import relationship

from datetime import datetime

from contextlib import contextmanager

UnsignedBigInteger = BigInteger()
UnsignedBigInteger = UnsignedBigInteger.with_variant(mysql.BIGINT(unsigned=True), 'mysql')
UnsignedBigInteger = UnsignedBigInteger.with_variant(sqlite.INTEGER(), 'sqlite')


def fk_guid(constraint, table):
    str_tokens = [
        table.name,
    ] + [
        element.parent.name for element in constraint.elements
    ] + [
        element.target_fullname for element in constraint.elements
    ]

    print(f'str_tokens: {str_tokens}')

    guid = uuid.uuid5(uuid.NAMESPACE_OID, "_".join(str_tokens))
    return str(guid)

convention = {
  "fk_guid": fk_guid,
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(column_0_name)s",
  "fk": "fk_%(fk_guid)s",
#  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

SessionMaker = sessionmaker()

Session = scoped_session(SessionMaker)

engine = None


class TableA(Base):
    __tablename__ = 'table_a'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    # table_b = Column(Integer, ForeignKey('table_b.id'), nullable=False)


class TableB(Base):
    __tablename__ = 'table_b'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)

