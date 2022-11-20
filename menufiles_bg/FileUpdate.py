from PyQt5.QtWidgets import QMessageBox
import datetime

def TextFile(self, titles, labels):

    lbl_bg, lbl_sea, lbl_sld = labels[0].text(), labels[1].text(), labels[2].text()

    if lbl_bg != "" or lbl_sea != "" or lbl_sld != "":
        txt = datetime.datetime.now().strftime("%c") + "\n"

        for n in range(3):
            if labels[n].text() != "":
                txt += titles[n] + " : " + "\n"
                txt += labels[n].text() + "\n"

        with open("order_bg.txt", "a") as file:
            file.write(txt)
    else:
        QMessageBox.information(self, "Грешка", "Не е записано нищо в поръчката!", QMessageBox.Ok, QMessageBox.Ok)