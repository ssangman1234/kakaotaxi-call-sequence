# admin.py - 관리자 대시보드
orders = []

def log_order(order):
    orders.append(order)

def get_all_orders():
    return orders
