
class Department:

    def __init__(self, departmentId, department_name, department_head_id, supervisor_name, email_address,
                 user_name, password):
        self.departmentId = departmentId
        self.department_name = department_name
        self.department_head_id = department_head_id
        self.supervisor_name = supervisor_name
        self.email_address = email_address
        self.user_name = user_name
        self.password = password

    def __repr__(self):
        return str({
            "departmentId": self.departmentId,
            "department_name": self.department_name,
            "department_head_id": self.department_head_id,
            "supervisor_name": self.supervisor_name,
            "email_address": self.email_address,
            "user_name": self.user_name,
            "password": self.password
        })

    def json(self):
        return {
            "departmentId": self.departmentId,
            "department_name": self.department_name,
            "department_head_id": self.department_head_id,
            "supervisor_name": self.supervisor_name,
            "email_address": self.email_address,
            "user_name": self.user_name,
            "password": self.password
        }
