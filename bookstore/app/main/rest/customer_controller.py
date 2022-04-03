from flask import request
from flask_restx import Namespace, Resource

from ..dto.customer_schema import CustomerSchema
from ..service.customer_service import add_new_customer, get_all_customers, get_customer_by_phone_number

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


@api.route('/<phone_number>')
@api.response(500, "An Error Occurred")
@api.response(404, 'Customer not found.')
class CustomerPhone(Resource):
    @api.doc("Get customer by phone number.")
    @api.marshal_list_with(CustomerSchema(api).get_mapping_schema())
    def get(self, phone_number):
        try:
            _customer = get_customer_by_phone_number(phone_number)
            if not _customer:
                api.abort(404)
            else:
                return _customer

        except Exception as err:
            api.logger.error(err)
            api.abort(500, message=err)