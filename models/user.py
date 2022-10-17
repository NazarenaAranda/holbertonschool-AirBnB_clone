#!/usr/bin/python3
"""create class user"""
from models.base_model import BaseModel


class user(BaseModel):
    """class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
