# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from database import Base
from sqlalchemy import Column, Integer, String, DateTime


class TagModel(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    url = Column(String)
    MD5 = Column(String(16), unique=True)

    def __init__(self, filename, url):
        self.filename = filename
        self.url = url

    def __repr__(self):
        return "<Tag ('%s','%s', '%s')>" % (self.filename, self.filename, self.filename)