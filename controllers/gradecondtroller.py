#
# from flask import request, jsonify
# from exceptions.resource_not_found import ResourceNotFound
# from exceptions.resource_unavailable import ResourceUnavailable
# from models.grades import Grades
# from implementations.graderepositimpl import GradeRepoImpl
# from services.gradeservice import GradeService
#
# gr = GradeRepoImpl()
# gs = GradeService(gr)
#
#
# def route(app):
#     @app.route("/grade", methods=['GET'])
#     def grade_by_event(grade_type):
#         try:
#             return gs.grade_by_event(grade_type).json(), 200
#         except ValueError as e:
#             return "Grade Cannot be Returned", 400
#         except ResourceUnavailable as i:
#             return i.message, 404
#
#     @app.route("/grade/<status>", methods=['GET'])
#     def grade_approval_status(grade_status):
#         try:
#             return gs.grade_approval_status(grade_status).json(), 200
#         except ValueError as e:
#             return "Status Cannot be Returned", 400
#         except ResourceNotFound as r:
#             return r.message, 404
#