from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

def LabelTitel (titel,css,order_list):

    order_ttl = QLabel(titel)
    order_ttl.setObjectName(css)

    if order_list != False:
        order_lbl = QLabel()
        order_list.addWidget(order_ttl)
        order_list.addWidget(order_lbl)
        return order_ttl, order_lbl

    else:
        order_ttl.setAlignment(Qt.AlignCenter)
        return order_ttl