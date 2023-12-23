#!/usr/bin/python3
""" Class definition of a City
"""
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ Defines the City table model for a mysql database
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")

State.cities = relationship("City", order_by=City.id, back_populates="state")
