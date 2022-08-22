def human_years_cat_years_dog_years(human_years):
    if human_years > 2:
        cat_years = (human_years-2)*4 + 15 + 9
        dog_years = (human_years-2)*5 + 15 + 9
    elif human_years == 2:
        cat_years = dog_years = 15 + 9
    else:
        cat_years = dog_years = 15
    return [human_years,cat_years,dog_years]