from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

def LabelTitel (titel,css,order_list):

    ord_ttl = QLabel(titel)
    ord_ttl.setObjectName(css)

    if order_list != False:
        ord_lbl = QLabel()
        order_list.addWidget(ord_ttl)
        order_list.addWidget(ord_lbl)
        return ord_ttl, ord_lbl

    else:
        ord_ttl.setAlignment(Qt.AlignCenter)
        return ord_ttl