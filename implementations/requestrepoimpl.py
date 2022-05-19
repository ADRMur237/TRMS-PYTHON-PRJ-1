# from abc import ABC
#
# from repositories.requestrepo import RequestRepo
# from util.db_connection import connection
# from models.request import Request
#
#
# def _build_request(request_record):
#     return Request(requestId=int(request_record[0]), employeeId=request_record[1],
#                    event_type=request_record[2], event_cost=request_record[3], amount=request_record[4],
#                    event_reimbursement=request_record[5], employee_grade=request_record[6],
#                    request_status=request_record[7])
#
#
# class RequestRepoImpl(RequestRepo, ABC):
#
#     def create_request(self, new_request):
#         sql = "INSERT INTO request VALUES (%s, %s, %s, %s, %s, %s, %s,) RETURNING *"
#         request_properties = [new_request.requestId, new_request.employeeId, new_request.event_type,
#                               new_request.event_cost, new_request.amount, new_request.event_reimbursement,
#                               new_request.employee_grade, new_request.request_status]
#
#         cursor = connection.cursor()
#         cursor.execute(sql, request_properties)
#
#         record = cursor.fetchone()
#
#         return _build_request(record)
#
#     def request_by_Id(self, requestId):
#         sql = "SELECT * FROM request WHERE requestId = %s"
#
#         cursor = connection.cursor()
#         cursor.execute(sql, requestId)
#
#         record = cursor.fetchone()
#
#         return _build_request(record)
#
#     def request_by_type(self, request_type):
#         sql = "SELECT * FROM request WHERE request_type = %s"
#
#         cursor = connection.cursor()
#         cursor.execute(sql, request_type)
#
#         record = cursor.fetchone()
#
#         return _build_request(record)
#
#     def amount_cost(self, amount):
#         sql = "SELECT * FROM request WHERE amount = %s"
#
#         cursor = connection.cursor()
#         cursor.execute(sql, amount)
#
#         record = cursor.fetchone()
#
#         return _build_request(record)
#
#     def request_reimbursement(self, event_reimbursement):
#         sql = "SELECT * FROM request WHERE reimbursement = %s"
#
#         cursor = connection.cursor()
#         cursor.execute(sql, event_reimbursement)
#
#         record = cursor.fetchone()
#
#         return _build_request(record)
#
#     def approval_status(self, request_status):
#         sql = "SELECT * FROM request WHERE request_status = %s"
#
#         cursor = connection.cursor()
#         cursor.execute(sql, request_status)
#
#         record = cursor.fetchone()
#
#         return _build_request(record)
