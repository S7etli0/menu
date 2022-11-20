from PyQt5.QtWidgets import QLabel, QMessageBox
from PyQt5.QtGui import QPixmap

def LoadImage(self,img,lay):
    try:
        with open(img):
            food_picture = QLabel()
            food_picture.setObjectName("Image")
            food_picture.setPixmap(QPixmap(img))
            lay.addWidget(food_picture)

    except FileNotFoundError:
        QMessageBox.information(self, "Error", "The image was not found in the directory!", QMessageBox.Ok, QMessageBox.Ok)
