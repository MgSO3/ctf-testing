from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping_host():
    host = request.form.get('host', '127.0.0.1')
    command = f"ping -c 1 {host}"
    
    try:
        output = os.popen(command).read()
        return output
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(port=5000)