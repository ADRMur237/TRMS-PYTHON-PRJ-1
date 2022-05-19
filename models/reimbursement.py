
class Reimbursement:

    def __init__(self, requestId, employeeId, event_cost,
                 event_reimbursement, employee_grade, request_status):
        self.requestId = requestId
        self.employeeId = employeeId
        self.event_cost = event_cost
        self.event_reimbursement = event_reimbursement
        self.employee_grade = employee_grade
        self.request_status = request_status

    def __repr__(self):
        return ({
            "requestId": self.requestId,
            "employeeId": self.employeeId,
            "event_cost": self.event_cost,
            "event_reimbursement": self.event_reimbursement,
            "employee_grade": self.employee_grade,
            "request_status": self.request_status
        })

    def json(self):
        return {
            "requestId": self.requestId,
            "employeeId": self.employeeId,
            "event_cost": self.event_cost,
            "event_reimbursement": self.event_reimbursement,
            "employee_grade": self.employee_grade,
            "request_status": self.request_status
        }
