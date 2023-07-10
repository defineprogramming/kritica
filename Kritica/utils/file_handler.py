import os
from Kritica.config.settings import upload_dir, download_dir

def upload_file(file, filename):
    try:
        file.save(os.path.join(upload_dir, filename))
        return True
    except Exception as e:
        print(e)
        return False

def download_file(filename):
    try:
        return open(os.path.join(download_dir, filename), 'rb')
    except Exception as e:
        print(e)
        return None