from models.reimbursement import Reimbursement


class TempDB:
    request = {
        1: Reimbursement(requestId=51078411, employeeId=1001, event_cost=1007, event_reimbursement=1000,
                         employee_grade="A", request_status="APPROVED"),
        2: Reimbursement(requestId=60178335, employeeId=1002, event_cost=1209, event_reimbursement=1000,
                         employee_grade="C", request_status="APPROVED"),
        3: Reimbursement(requestId=49925661, employeeId=2001, event_cost=1150, event_reimbursement=1000,
                         employee_grade="B", request_status="APPROVED"),
        4: Reimbursement(requestId=36378921, employeeId=1004, event_cost=1457, event_reimbursement=1000,
                         employee_grade="D", request_status="DENIED"),
        5: Reimbursement(requestId=22071407, employeeId=2002, event_cost=1067, event_reimbursement=1000,
                         employee_grade="A", request_status="APPROVED")
    }
