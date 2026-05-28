from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/download')
def download_file():
    filename = request.args.get('file')
    filepath = os.path.join('/var/www/html/files/', filename)
    
    if os.path.exists(filepath):
        return send_file(filepath)
    return "File not found", 404