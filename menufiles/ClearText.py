from PyQt5.QtWidgets import QMessageBox

def ClearRadArea(self,label):
    num = len(label)
    full_order = ""

    if num>1:
        full_order = label[0].text()+label[1].text()+label[2].text()

    if num>1 and full_order == "":
        QMessageBox.information(self, "Error", "All orders have already been deleted!", QMessageBox.Ok, QMessageBox.Ok)

    else:
        for x in label:
            if num == 1 and x.text() == "":
                QMessageBox.information(self, "Error", "This order has already been deleted!", QMessageBox.Ok, QMessageBox.Ok)
            else:
                x.setText("")

    if num == 1:
        return ""
    else:
        return "","",""