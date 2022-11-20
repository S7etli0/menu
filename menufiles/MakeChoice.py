def MealChoice(meal, many):

    if many:
        meal.setExclusive(False)
        for x in meal.buttons():
            x.setChecked(False)
    else:
        for x in meal.buttons():
            x.setChecked(False)
        meal.setExclusive(True)