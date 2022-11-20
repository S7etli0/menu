from PyQt5.QtWidgets import QRadioButton, QVBoxLayout

def MenuRadBox(check,all_food,group):

    food_lay = QVBoxLayout()
    for x in all_food:
        food = QRadioButton(x)

        if check:
            food.setObjectName("RadTitle")

        group.addButton(food)
        food_lay.addWidget(food)
        
    return food_lay