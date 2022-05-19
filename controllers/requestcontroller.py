#
# from flask import request, jsonify
# from exceptions.resource_not_found import ResourceNotFound
# from exceptions.resource_unavailable import ResourceUnavailable
# from models.request import Request
# from implementations.requestrepoimpl import RequestRepoImpl
# from services.requestservices import RequestService
#
# rqr = RequestRepoImpl()
# rqs = RequestService(rqr)
#
#
# def route(app):
#
#     @app.route("/request/<create_new>", methods=["POST"])
#     def create_request():
#         body = request.json
#
#         request = Request(requestId=body[0], employeeId=body[1], event_type=body[2], event_cost=body[3],
#                           amount=body[4], event_reimbursement=body[5], employee_grade=body[6], request_status=body[7])
#         request = rqs.create_request(request)
#
#         return jsonify(request.json(), 200)
#
#     @app.route("/request/<request_id>", methods=["GET"])
#     def request_by_id(requestId):
#         try:
#             return rqs.request_by_Id(int(requestId)).json(), 200
#         except ValueError as e:
#             return "Not a Valid Request ID", 400
#         except ResourceNotFound as r:
#             return r.message, 404
#
#     @app.route("/request/<type>", methods=['GET'])
#     def request_by_type(request_type):
#         try:
#             return rqs.request_by_type(int(request_type)).json(), 200
#         except ValueError as e:
#             return "Request Cannot be Completed", 400
#         except ResourceNotFound as r:
#             return r.message, 404
#
#     @app.route("/request/<event>", methods=['GET'])
#     def request_by_event(event_type):
#         try:
#             return rqs.request_by_event(int(event_type)).json(), 200
#         except ValueError as e:
#             return "Request Cannot be Completed", 400
#         except ResourceNotFound as r:
#             return r.message, 404
#
#     @app.route("/amount", methods=['GET'])
#     def amount_cost(amount):
#         try:
#             return rqs.amount_cost(amount).json(), 200
#         except ValueError as e:
#             return "Amount is not Verified", 400
#         except ResourceUnavailable as i:
#             return i.message, 404
#
#     @app.route("request/<reimbursement>", methods=['GET'])
#     def request_reimbursement(event_reimbursement):
#         try:
#             return rqs.request_reimbursement(event_reimbursement).json(), 200
#         except ValueError as e:
#             return "Request Cannot Be Completed", 400
#         except ResourceUnavailable as i:
#             return i.message, 404
#
#     @app.route("/request/<approval>", methods=['GET'])
#     def approval_status(request_status):
#         try:
#             return rqs.approval_status(request_status).json(), 200
#         except ResourceUnavailable as i:
#             return i.message, 400
#         except ResourceNotFound as r:
#             return r.message, 404
