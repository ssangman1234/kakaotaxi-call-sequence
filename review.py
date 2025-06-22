# review.py - 사용자 리뷰 시스템
reviews = {}

def submit_review(order_id, rating, comment):
    reviews[order_id] = {"rating": rating, "comment": comment}
