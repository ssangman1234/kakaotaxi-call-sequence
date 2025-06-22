# fare.py - 요금 계산 시스템
def calculate_fare(distance_km, duration_min):
    base_fare = 3000
    per_km = 1000
    per_min = 100
    return base_fare + per_km * distance_km + per_min * duration_min
