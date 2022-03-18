import unittest

from app import blueprint
from app.main import create_app

rest_port = 5012

app = create_app('dev')
app.register_blueprint(blueprint)

app.app_context().push()


def run():
    app.run(port=rest_port)


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    run()
