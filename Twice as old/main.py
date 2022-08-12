def twice_as_old(dad_years_old, son_years_old):
    for i in range(dad_years_old+1):
        if (dad_years_old + i)/2 == (son_years_old + i):
            return i
    for i in range(dad_years_old+1):
        if (dad_years_old - i)/2 == (son_years_old - i):
            return i