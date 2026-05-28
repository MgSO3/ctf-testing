import pickle
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/restore', methods=['POST'])
def restore_backup():
    data = request.form.get('backup_data')
    try:
        decoded = base64.b64decode(data)
        obj = pickle.loads(decoded)
        return "Backup restored!"
    except Exception as e:
        return str(e)