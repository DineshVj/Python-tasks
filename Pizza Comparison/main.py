def which_pizza(d1,price1,d2,price2):
    price_1 = (((d1/2)**2)*3.14)/price1
    price_2 = (((d2/2)**2)*3.14)/price2
    if price_1 > price_2:
        return d1
    else:
        return d2
