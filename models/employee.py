
class Employee:
    def __init__(self, employeeId, full_name, email_address,
                 user_name, password, supervisor, departmentId):
        self.employeeId = employeeId
        self.full_name = full_name
        self.email_address = email_address
        self.user_name = user_name
        self.password = password
        self.supervisor = supervisor
        self.departmentId = departmentId

    def __repr__(self):
        return str({
            "employeeId": self.employeeId,
            "full_name": self.full_name,
            "email_address": self.email_address,
            "user_name": self.user_name,
            "password": self.password,
            "supervisor": self.supervisor,
            "departmentId": self.departmentId
        })

    def json(self):
        return {
            "employeeId": self.employeeId,
            "full_name": self.full_name,
            "email_address": self.email_address,
            "user_name": self.user_name,
            "password": self.password,
            "supervisor": self.supervisor,
            "departmentId": self.departmentId
        }
