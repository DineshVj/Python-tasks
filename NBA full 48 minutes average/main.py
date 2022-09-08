def nba_extrap(ppg, mpg):
    if ppg > 0 and mpg > 0:
        ppm = ppg/mpg
        return round(ppm*48,1)
    else:
        return 0