import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    pwd = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    favourites = relationship('Favourite', backref='user', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    diameter = Column(String(250), nullable=True)
    climate = Column(String(250), nullable=True)
    population = Column(String(250), nullable=True)
    persons = relationship('Person', backref='planet', lazy=True)
    favourites = relationship('Favourite', backref='planet', lazy=True)

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    height = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    hair_color = Column(String(250), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    vehicles = relationship('Vehicle', backref='person')
    favourites = relationship('Favourite', backref='person', lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    length = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    favourites = relationship('Favourite', backref='vehicle', lazy=True)

class Favourite(Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
