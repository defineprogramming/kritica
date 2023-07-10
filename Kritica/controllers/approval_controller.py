```python
from Kritica.services.approval_service import ApprovalService
from Kritica.models.approval import Approval
from Kritica.utils.validator import validate_approval

class ApprovalController:
    def __init__(self):
        self.approval_service = ApprovalService()

    def handle_approval(self, approval_data):
        approval = Approval(approval_data)
        validation_errors = validate_approval(approval)
        if validation_errors:
            return {"status": "error", "message": "approval_error", "errors": validation_errors}
        else:
            approval_result = self.approval_service.approve_book(approval)
            if approval_result:
                return {"status": "success", "message": "approval_success"}
            else:
                return {"status": "error", "message": "approval_error"}
```