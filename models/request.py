#
# class Request:
#
#     def __init__(self, requestId, employeeId, event_type, event_cost,
#                  amount, event_reimbursement, employee_grade, request_status):
#         self.requestId = requestId
#         self.employeeId = employeeId
#         self.event_type = event_type
#         self.event_cost = event_cost
#         self.amount = amount
#         self.event_reimbursement = event_reimbursement
#         self.employee_grade = employee_grade
#         self.request_status = request_status
#
#     def __repr__(self):
#         return ({
#             "requestId": self.requestId,
#             "employeeId": self.employeeId,
#             "event_type": self.event_type,
#             "event_cost": self.event_cost,
#             "amount": self.amount,
#             "event_reimbursement": self.event_reimbursement,
#             "employee_grade": self.employee_grade,
#             "request_status": self.request_status
#         })
#
#     def json(self):
#         return {
#             "requestId": self.requestId,
#             "employeeId": self.employeeId,
#             "event_type": self.event_type,
#             "event_cost": self.event_cost,
#             "amount": self.amount,
#             "event_reimbursement": self.event_reimbursement,
#             "employee_grade": self.employee_grade,
#             "request_status": self.request_status
#         }
