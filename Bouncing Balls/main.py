def bouncing_ball(h, bounce, window):
    counter = 0
    current = h
    if h>0 and bounce < 1 and bounce > 0 and window < h:
        while True:
            current = current*bounce
            print(current)
            if current > window:
                counter +=2
            elif current < window:
                break
        return counter +1
    else:
        return -1