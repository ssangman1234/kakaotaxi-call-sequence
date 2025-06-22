# status.py - 호출 상태 관리
order_status = {}

def update_status(order_id, status):
    order_status[order_id] = status

def get_status(order_id):
    return order_status.get(order_id, "unknown")
