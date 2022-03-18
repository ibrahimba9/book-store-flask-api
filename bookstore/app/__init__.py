from flask_restx import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Preprocessing RESTFul API',
          version='1.0',
          description='Preprocessing RESTFul web service.'
          )

# api.add_namespace(data_combination_ns, path='/data-combination')