from flask import Flask
from Kritica.config import settings
from Kritica.views import upload_view, download_view, approval_view

app = Flask(__name__)
app.config.from_object(settings)

app.register_blueprint(upload_view.bp)
app.register_blueprint(download_view.bp)
app.register_blueprint(approval_view.bp)

if __name__ == "__main__":
    app.run(debug=True)