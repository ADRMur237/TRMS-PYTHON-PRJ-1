# from datetime import datetime
# from time import time
#
# from exceptions.resource_unavailable import ResourceUnavailable
# from repositories.requestrepo import RequestRepo
# from implementations.requestrepoimpl import RequestRepoImpl
#
#
# class RequestService:
#
#     def __init__(self, request_repo: RequestRepo):
#         self.request_repo = request_repo
#
#     def create_request(self, new_request):
#         return self.request_repo.create_request(new_request)
#
#     def request_by_Id(self, requestId):
#         return self.request_repo.request_by_Id(requestId)
#
#     def request_by_type(self, request_type):
#         return self.request_repo.request_by_type(request_type)
#
#     def request_by_event(self, event_type):
#         return self.request_repo.request_by_event(event_type)
#
#     def amount_cost(self, amount):
#         return self.request_repo.amount_cost(amount)
#
#     def request_reimbursement(self, event_reimbursement):
#         # return self.request_repo.request_reimbursement(event_reimbursement)
#         reimbursement = self.request_reimbursement(event_reimbursement)
#         if reimbursement.approved:
#             reimbursement.approved = False
#             reimbursement.approval_date = int(time()) + 604800
#             self.request_reimbursement(reimbursement)
#             return reimbursement
#         else:
#             raise ResourceUnavailable(f"Approval is not updated. Status will update: "
#                                       f"{datetime.fromtimestamp(reimbursement.approval_date)}")
#
#     def approval_status(self, request_status):
#         # return self.request_repo.approval_status(request_status)
#         return self.request_repo.approval_status(request_status)
