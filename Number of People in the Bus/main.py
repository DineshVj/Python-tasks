def number(bus_stops):
    counter = 0
    for el in bus_stops:
        counter += el[0]
        counter -= el[1]
    return counter