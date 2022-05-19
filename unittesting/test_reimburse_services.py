import unittest
from unittest.mock import MagicMock

from models.reimbursement import Reimbursement
from implementations.reimburserepoimpl import ReimburseRepoImpl
from services.reimburservices import ReimburseService


class TestReimbursement(unittest.TestCase):
    rr = ReimburseRepoImpl()
    rs = ReimburseService(rr)

    def test_get_reimbursement(self):
        self.get_reimbursement = MagicMock(return_value=[
            Reimbursement(requestId=51078411, employeeId=1001, event_cost=1007, event_reimbursement=1000,
                          employee_grade="A", request_status="APPROVED"),
            Reimbursement(requestId=60178335, employeeId=1002, event_cost=1209, event_reimbursement=1000,
                          employee_grade="C", request_status="APPROVED"),
            Reimbursement(requestId=49925661, employeeId=2001, event_cost=1150, event_reimbursement=1000,
                          employee_grade="B", request_status="APPROVED")
        ])

        refined_reimbursement = self.rs.request_reimbursement(1012)
        print(refined_reimbursement)

        self.assertListEqual(refined_reimbursement, [
            Reimbursement(requestId=7086113, employeeId=1012, event_cost=1322, event_reimbursement=1000,
                          employee_grade="C", request_status="APPROVED"),
            Reimbursement(requestId=[], employeeId=[], event_cost=[], event_reimbursement=[],
                          employee_grade=[], request_status=[])
        ])

    def test_update_grade_status(self):
        self.update_grade_status = MagicMock()

    def test_get_approval_status(self):
        self.approval_status = MagicMock()


if __name__ == '__main__':
    unittest.main()
