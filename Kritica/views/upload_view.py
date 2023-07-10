```python
from flask import Blueprint, render_template, request
from Kritica.controllers.upload_controller import handle_upload

upload_view = Blueprint('upload_view', __name__)

@upload_view.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        title = request.form['title']
        author = request.form['author']
        file_format = request.form['file_format']
        uploader_id = request.form['uploader_id']
        message = handle_upload(file, title, author, file_format, uploader_id)
        return render_template('upload.html', message=message)
    return render_template('upload.html')
```