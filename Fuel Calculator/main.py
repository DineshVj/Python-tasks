import math


def fuel_price(litres, price_per_litre):
    discount = math.floor(litres / 2)*5
    if discount >= 25:
        discount = 25
    return round(litres * (price_per_litre - (discount/100)), 2)