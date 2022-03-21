from app.main import db
from app.main.model.customer import Customer


def add_new_customer(input_data):
    customer = Customer.query.filter_by(phone_number=input_data['phone_number']).first()

    if not customer:
        new_customer = Customer(
            email=input_data['email'],
            name=input_data['name'],
            phone_number=input_data['phone_number']
        )
        # new_customer = Customer(input_data**) same as the previous line if the object's attributes labels are equal to the schema's fields labels
        commit_changes(new_customer)
        response_object = {
            'status': 'success',
            'message': 'New customer successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Customer with phone number {} already exists.'.format(input_data['phone_number']),
        }
        return response_object, 409


def commit_changes(data):
    db.session.add(data)
    db.session.commit()


def get_all_customers():
    return Customer.query.all()


def get_customer_by_phone_number(phone_number):
    return Customer.query.filter_by(phone_number=phone_number).first()
