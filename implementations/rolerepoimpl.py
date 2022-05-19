#
# from abc import ABC
#
# from repositories.rolereposit import RoleRepo
# from util.db_connection import connection
# from models.role import Role
#
#
# def _employee_role(role):
#     return Role(supervisor_id=role.supervisor_id[0], role=role.role[1])
#
#
# class RoleRepoImpl(RoleRepo, ABC):
#     def supervisor_by_id(self, supervisor_id):
#         sql = "SELECT * FROM role WHERE supervisor_id = %s"
#
#         cursor = connection.cursor()
#         cursor.execute(sql, supervisor_id)
#
#         record = cursor.fetchone()
#
#         return _employee_role(record)
#
#     def role_by_grade(self, role):
#         sql = "SELECT * FROM role WHERE role = %s"
#
#         cursor = connection.cursor()
#         cursor.execute(sql, role)
#
#         record = cursor.fetchone()
#
#         return _employee_role(record)
