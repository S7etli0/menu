from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

def SetSectionTitel (titel,describe):

    desc = QWidget()
    desc.setObjectName("TabOra")
    desc.setObjectName("Boarder")
    desc_wd = QVBoxLayout()
    desc.setLayout(desc_wd)

    head_text = QLabel(titel)
    head_text.setAlignment(Qt.AlignCenter)
    head_text.setObjectName("InTitle")

    text = QLabel(describe)
    text.setAlignment(Qt.AlignCenter)
    desc_wd.addWidget(head_text)
    desc_wd.addWidget(text)

    return desc
