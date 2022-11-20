from PyQt5.QtWidgets import QMessageBox

def AddtoOrder(self, food, order_lbl):

    collect = order_lbl.text()
    new_dishes = ""

    for x in food.buttons():
        if x.isChecked():
            new_dishes += "+ " + x.text() + "\n"
    collect += new_dishes

    if new_dishes == "" :
        QMessageBox.information(self, "Грешка", "Не е избрано нищо от менюто!", QMessageBox.Ok, QMessageBox.Ok)
    else:
        order_lbl.setText(collect)