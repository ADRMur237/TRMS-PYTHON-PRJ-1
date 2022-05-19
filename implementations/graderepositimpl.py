#
# from abc import ABC
#
# from repositories.gradereposit import GradeRepo
# from util.db_connection import connection
# from models.grades import Grades
#
#
# def _grade_approval(grades):
#     return Grades(grade_type=grades.grade_type[2], grade_status=grades.grade_status[1])
#
#
# class GradeRepoImpl(GradeRepo, ABC):
#     def grade_by_event(self, grade_type):
#         sql = "SELECT * FROM grades WHERE grade_type = %s"
#
#         cursor = connection.cursor()
#         cursor.execute(sql, grade_type)
#
#         record = cursor.fetchone()
#
#         return _grade_approval(record)
#
#     def grade_approval_status(self, grade_status):
#         sql = "SELECT * FROM grades WHERE grade status = %s"
#
#         cursor = connection.cursor()
#         cursor.execute(sql, grade_status)
#
#         record = cursor.fetchone()
#
#         return _grade_approval(record)
