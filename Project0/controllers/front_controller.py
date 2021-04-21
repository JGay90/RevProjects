from controllers import user_controller as uc
from controllers import account_controller as ac


def route(app):
    # Calls all other other controllers
    uc.route(app)
    ac.route(app)


