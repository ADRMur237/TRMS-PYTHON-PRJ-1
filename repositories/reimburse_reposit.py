from abc import abstractmethod


class ReimburseRepo:

    @abstractmethod
    def create_request(self, new_request):
        pass

    @abstractmethod
    def request_by_Id(self, requestId):
        pass

    @abstractmethod
    def employee_request(self, employeeId):
        pass

    @abstractmethod
    def amount_cost(self, event_cost):
        pass

    @abstractmethod
    def request_reimbursement(self, event_reimbursement):
        pass

    @abstractmethod
    def update_grade_status(self, employee_grade):
        pass

    @abstractmethod
    def approval_status(self, request_status):
        pass
