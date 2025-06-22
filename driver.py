# driver.py - 기사 정보 관리
drivers = [
    {"id": 1, "name": "홍길동", "car": "서울 12가 3456", "rating": 4.9, "location": 3},
    {"id": 2, "name": "이몽룡", "car": "서울 34나 6789", "rating": 4.7, "location": 5}
]

def get_driver(driver_id):
    return next((d for d in drivers if d["id"] == driver_id), None)
