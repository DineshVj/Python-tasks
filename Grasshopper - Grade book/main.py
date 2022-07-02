def get_grade(s1, s2, s3):
    points = (s1 + s2 + s3) / 3
    if points >= 90:
        return 'A'
    elif points >= 80:
        return 'B'
    elif points >= 70:
        return 'C'
    elif points >= 60:
        return 'D'
    elif points >= 0:
        return 'F'