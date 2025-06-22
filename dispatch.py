# dispatch.py - 기사 배차 알고리즘
def dispatch(user_location, driver_list):
    nearest_driver = min(driver_list, key=lambda d: abs(d["location"] - user_location))
    return nearest_driver
