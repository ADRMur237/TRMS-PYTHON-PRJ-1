from abc import ABC

from repositories.reimburse_reposit import ReimburseRepo
from util.db_connection import connection
from models.reimbursement import Reimbursement


def _build_request(request_record):
    return Reimbursement(requestId=int(request_record[0]), employeeId=request_record[1], event_cost=request_record[2],
                         event_reimbursement=request_record[3], employee_grade=request_record[4],
                         request_status=request_record[5])


class ReimburseRepoImpl(ReimburseRepo, ABC):

    def create_request(self, new_request):
        sql = "INSERT INTO request VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
        request_properties = [new_request.requestId, new_request.employeeId,
                              new_request.event_cost, new_request.event_reimbursement,
                              new_request.employee_grade, new_request.request_status]

        cursor = connection.cursor()
        cursor.execute(sql, request_properties)

        connection.commit()
        record = cursor.fetchone()

        return _build_request(record)

    def request_by_Id(self, requestId):
        sql = "SELECT * FROM reimbursement WHERE requestId = %s"

        cursor = connection.cursor()
        cursor.execute(sql, requestId)

        connection.commit()
        record = cursor.fetchone()

        return _build_request(record)

    def employee_request(self, employeeId):
        sql = "SELECT * FROM reimbursement WHERE employeeId = %s"

        cursor = connection.cursor()
        cursor.execute(sql, employeeId)

        connection.commit()
        record = cursor.fetchone()

        return _build_request(record)

    def amount_cost(self, event_cost):
        sql = "SELECT * FROM reimbursement WHERE amount = %s"

        cursor = connection.cursor()
        cursor.execute(sql, event_cost)

        connection.commit()
        record = cursor.fetchone()

        return _build_request(record)

    def request_reimbursement(self, event_reimbursement):
        sql = "SELECT * FROM reimbursement WHERE reimbursement = %s"

        cursor = connection.cursor()
        cursor.execute(sql, event_reimbursement)

        connection.commit()
        record = cursor.fetchone()

        return _build_request(record)

    def update_grade_status(self, employee_grade):
        sql = "SELECT * FROM reimbursement WHERE employee_grade = %s"

        cursor = connection.cursor()
        cursor.execute(sql, employee_grade)

        connection.commit()
        record = cursor.fetchone()

        return _build_request(record)

    def approval_status(self, request_status):
        sql = "SELECT * FROM reimbursement WHERE request_status = %s"

        cursor = connection.cursor()
        cursor.execute(sql, request_status)

        connection.commit()
        record = cursor.fetchone()

        return _build_request(record)
