from flask import Blueprint
from flask_restx import Api

from app.main.rest.customer_controller import api as customer_ns  # customer namespace

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Book Store RESTFul API',
          version='1.0',
          description='Book Store RESTFul web service.'
          )

api.add_namespace(customer_ns, path='/customer')
