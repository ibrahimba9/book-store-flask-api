from marshmallow import Schema
from flask_restx import fields


class CustomerSchema(Schema):
    def __init__(self, namespace):
        super().__init__()
        self.namespace = namespace

    def get_mapping_schema(self):
        return self.namespace.model('CustomerSchema', {
            'name': fields.String(required=True, description="Name of a customer."),
            'email': fields.String(required=True, description="Email of a customer."),
            'phone_number': fields.Integer(required=True, description="Unique phone number of a customer.")
        })
