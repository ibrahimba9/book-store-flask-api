from flask import request
from flask_restx import Namespace, Resource

from ..dto.customer_schema import CustomerSchema
from ..service.customer_service import add_new_customer, get_all_customers

api = Namespace('CustomerApi', 'Customer related endpoints')


@api.route('/')
@api.response(500, "An Error Occurred")
class Customer(Resource):
    @api.doc("Add a new customer.")
    @api.expect(CustomerSchema(api).get_mapping_schema(), location="query", as_dict=True)
    def post(self):
        request_body = request.json
        try:
            add_new_customer(request_body)
        except Exception as err:
            api.logger.error(err)
            api.abort(500, message=err)

    @api.doc("Get list of all customers.")
    @api.marshal_list_with(CustomerSchema(api).get_mapping_schema())
    def get(self):
        try:
            return get_all_customers()
        except Exception as err:
            api.logger.error(err)
            api.abort(500, message=err)
