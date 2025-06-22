# auth.py - 사용자 로그인 시스템
users = {"user1": "pass123"}

def login(username, password):
    return users.get(username) == password
