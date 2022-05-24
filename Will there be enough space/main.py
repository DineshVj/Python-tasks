def enough(cap, on, wait):
    if on+wait>cap:
        return abs(cap-on-wait)
    else:
        return 0