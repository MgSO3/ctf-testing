import requests
from flask import Flask, request

app = Flask(__name__)
ALLOWED_DOMAINS = ["https://trusted-images.com/"]

@app.route('/fetch_image')
def fetch():
    url = request.args.get('url', '')
    
    if not any(url.startswith(domain) for domain in ALLOWED_DOMAINS):
        return "Error: Domain not allowed", 403
        
    try:
        resp = requests.get(url, timeout=3)
        return resp.content
    except:
        return "Failed to fetch", 500