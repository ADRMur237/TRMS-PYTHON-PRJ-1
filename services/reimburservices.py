from datetime import datetime
from time import time

from exceptions.resource_unavailable import ResourceUnavailable
from repositories.reimburse_reposit import ReimburseRepo


class ReimburseService:

    def __init__(self, reimburse_repo: ReimburseRepo):
        self.reimburse_repo = reimburse_repo

    def create_request(self, new_request):
        return self.reimburse_repo.create_request(new_request)

    def request_by_Id(self, requestId):
        return self.reimburse_repo.request_by_Id(requestId)

    def employee_request(self, employeeId):
        return self.reimburse_repo.employee_request(employeeId)

    def amount_cost(self, event_cost):
        return self.reimburse_repo.amount_cost(event_cost)

    def request_reimbursement(self, event_reimbursement):
        # return self.reimburse_repo.request_reimbursement(event_reimbursement)
        rmb = self.request_reimbursement(event_reimbursement)
        rmb.request_date = time()

        amount = self.reimburse_repo.amount_cost(event_reimbursement)
        amount.rmb = time()

        if amount > 1000:
            amount.event_cost = 1000
            return self.reimburse_repo.amount_cost(event_reimbursement)
        else:
            amount.event_cost = amount
            return self.reimburse_repo.amount_cost(event_reimbursement)

    def update_grade_status(self, employee_grade):
        # return self.reimburse_repo.update_grade_status(employee_grade)
        rmb = self.reimburse_repo.update_grade_status(employee_grade)
        rmb.request_date = time()

        if rmb.approved:
            rmb.approved = False
            rmb.approval_date = int(time())
            self.request_reimbursement(rmb)
            return rmb
        else:
            raise ResourceUnavailable(f"Approval is not updated. Status will update: "
                                      f"{datetime.fromtimestamp(rmb.approval_date)}")

    def approval_status(self, request_status):
        # return self.request_repo.approval_status(request_status)
        rmb = self.update_grade_status(request_status)
        if rmb.grade == "A" or "B" or "C":
            rmb.request_status = "Approval Status Pending"
            return self.update_grade_status(request_status)
        else:
            rmb.status = "Approval Denied"
            return self.update_grade_status(request_status)


def _test():
    rr = ReimburseRepo()
    rs = ReimburseService(rr)

    print(rs.request_reimbursement())

    print("---------------")
    print(rs.request_by_Id(7086113))
    print(rs.employee_request(112))
    print(rs.update_grade_status("C"))

    print(int(time()))

    rs.approval_status(112)
    print(rs.approval_status(112))


if __name__ == '__main__':
    _test()
