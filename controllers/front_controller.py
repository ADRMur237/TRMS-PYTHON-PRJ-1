
from controllers import departmentcontroller, employeecontroller, reimbursecontroller


def route(app):
    departmentcontroller.route(app)
    employeecontroller.route(app)
    reimbursecontroller.route(app)
