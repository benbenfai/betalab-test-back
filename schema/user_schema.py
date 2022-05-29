from flask_marshmallow import Marshmallow
from marshmallow import validate,fields

ma = Marshmallow()

class LoginSchema(ma.Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    """
    password = fields.Str(required=True,
    validate=[validate.Length(min=6, max=36)])
    """

class registerSchema(ma.Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    address = fields.Str(required=True)
    phone = fields.Str(required=True)
    picture = fields.Str(required=True) 
    company = fields.Str(required=True)