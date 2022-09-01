import math

def calculate_tip(amount, rating):
    rating = rating.title()
    if rating == "Terrible":
        percent = 0
    elif rating == "Poor":
        percent = 0.05
    elif rating == "Good":
        percent = 0.1
    elif rating == "Great":
        percent = 0.15
    elif rating == "Excellent":
        percent = 0.2
    else:
        return "Rating not recognised"
    return math.ceil(percent*amount)