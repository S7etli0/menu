from PyQt5.QtWidgets import QWidget, QVBoxLayout

def AddLayWidget(style):

    if len(style) == 1:

        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        tab.setObjectName(style[0])

        return tab, layout

    else:
        layout, all_items = style[0], style[1]

        for item in all_items:
            layout.addWidget(item)