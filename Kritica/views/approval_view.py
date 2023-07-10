```python
from flask import Blueprint, render_template, request, flash, redirect, url_for
from Kritica.models.approval import Approval
from Kritica.controllers.approval_controller import handle_approval

approval_view = Blueprint('approval_view', __name__)

@approval_view.route('/approval', methods=['GET', 'POST'])
def approval():
    if request.method == 'POST':
        book_id = request.form.get('book_id')
        approver_id = request.form.get('approver_id')
        status = request.form.get('status')

        approval = Approval(book_id, approver_id, status)
        message = handle_approval(approval)

        flash(message)
        return redirect(url_for('approval_view.approval'))

    return render_template('approval.html')
```