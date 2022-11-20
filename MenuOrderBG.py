from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QGridLayout, \
        QPushButton, QButtonGroup, QGroupBox, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
import sys


from menufiles_bg.OrderCss import order_style
from menufiles_bg.OrderLabels import LabelTitel
from menufiles_bg.TabTitle import SetSectionTitel
from menufiles_bg.AddItems import AddtoOrder
from menufiles_bg.MenuImage import LoadImage
from menufiles_bg.MakeChoice import MealChoice
from menufiles_bg.DishesBox import MenuRadBox
from menufiles_bg.LayWidget import AddLayWidget
from menufiles_bg.ClearText import ClearRadArea
from menufiles_bg.FileUpdate import TextFile


class Ordering(QWidget):
    def __init__(self):
        super().__init__()
        self.OrderMenu()


    def OrderMenu(self):
        self.setGeometry(50,50,400,800)
        self.setWindowIcon(QIcon("foodmenu/foodicon.png"))
        self.setWindowTitle("Избери Ястие и Поръчай")
        self.MenuItems()
        self.show()


    def MenuItems(self):
#       Поръчка
        order_tab, order_main = AddLayWidget(["TabRed"])
        order_tab_sm, order_list = AddLayWidget(["TabOra"])
        mylist, order_lay = AddLayWidget(["Side"])
        order_main.addWidget(mylist)

        self.order_ttl_bg, order_lbl_bg = LabelTitel("Българска Кухня", "SmTitle", order_list)
        self.order_ttl_sea, order_lbl_sea = LabelTitel("Морска Кухня", "SmTitle", order_list)
        self.order_ttl_sld, order_lbl_sld = LabelTitel("Салатен Бар", "SmTitle", order_list)


#       Български Ястия
        bg_tab, bg_lay = AddLayWidget(["TabRed"])
        bg_food = ["винен кебап","пилешко вретено","мешана скара","царски гювеч","дроб сърма","агнешко филе"]
        bg_food_veg = ["пълнени чушки","плато гъби","кашкавал пане","картофен огретен"]
        bg_meatfood = QButtonGroup()

        bg_lay_food = MenuRadBox(False, bg_food, bg_meatfood)
        bg_lay_veg = MenuRadBox(False, bg_food_veg, bg_meatfood)

        bg_text = "Традиционни ястия от всички краища на България"
        bg_desc = SetSectionTitel("Българска Кухня",bg_text)
        bg_lay.addWidget(bg_desc)

        bg_food_pic = "foodmenu/bg-food.png"
        LoadImage(self, bg_food_pic, bg_lay)

        bg_meatbox = QGroupBox("Месни Ястия")
        bg_vegbox = QGroupBox("Ястия без Месо")

        AddLayWidget([bg_lay, [bg_meatbox, bg_vegbox]])
        bg_meatbox.setLayout(bg_lay_food)
        bg_vegbox.setLayout(bg_lay_veg)

        bg_bttns = QHBoxLayout()
        bg_multi,bg_single,bg_order = self.MakeButtons(self, bg_meatfood, order_lbl_bg)

        AddLayWidget([bg_bttns,[bg_multi,bg_single,bg_order]])
        bg_lay.addLayout(bg_bttns)
        bg_lay.addStretch()


#       Морски Ястия
        sea_tab, sea_lay = AddLayWidget(["TabRed"])
        sea_food = ["барбун", "лаврак", "херинга", "цаца", "попчета", "калкан"]
        sea_food_veg = ["калмари", "скариди", "миди", "раци"]
        sea_meatfood = QButtonGroup()

        sea_layfish = MenuRadBox(False, sea_food, sea_meatfood)
        sea_vegfish = MenuRadBox(False, sea_food_veg, sea_meatfood)

        sea_text = "Любими ястия на рибарите и моряците в България"
        sea_desc = SetSectionTitel("Морска Кухня", sea_text)
        sea_lay.addWidget(sea_desc)

        seapic = "foodmenu/sea-food.png"
        LoadImage(self, seapic, sea_lay)

        sea_box = QGroupBox("Рибни Ястия")
        sea_vegbox = QGroupBox("Морски Дарове")

        AddLayWidget([sea_lay,[sea_box,sea_vegbox]])
        sea_box.setLayout(sea_layfish)
        sea_vegbox.setLayout(sea_vegfish)

        sea_bttns = QHBoxLayout()
        sea_multi, sea_single, sea_order = self.MakeButtons(self, sea_meatfood, order_lbl_sea)

        AddLayWidget([sea_bttns,[sea_multi,sea_single,sea_order]])
        sea_lay.addLayout(sea_bttns)
        sea_lay.addStretch()


#       Салатен Бар
        salad_tab, salad_mainlay = AddLayWidget(["TabRed"])
        salads = ["шопска","снежанка","руска","манастирска","овчарска","градинска","царска туршия"]
        salad_food = QButtonGroup()

        salad_lay = MenuRadBox(False, salads, salad_food)
        salad_text = "Избор на салати по рецепти на Български земеделци"
        sld_desc = SetSectionTitel("Салатен Бар", salad_text)
        salad_mainlay.addWidget(sld_desc)

        seapic = "foodmenu/salad.png"
        LoadImage(self, seapic, salad_mainlay)

        saladbox = QGroupBox("Добави Гарнитура")
        saladbox.setLayout(salad_lay)
        salad_mainlay.addWidget(saladbox)

        sld_bttns = QHBoxLayout()
        salad_multi,salad_single,salad_order = self.MakeButtons(self, salad_food, order_lbl_sld)

        AddLayWidget([sld_bttns, [salad_multi,salad_single,salad_order]])
        salad_mainlay.addLayout(sld_bttns)
        salad_mainlay.addStretch()


#       Поръчка
        order_ttl = LabelTitel("Вашият Избор","Title",False)
        order_lay.addWidget(order_ttl)

        order_lay.addWidget(order_tab_sm)
        order_lay.addStretch()

        click_order = QPushButton("Поръчай")
        ttl_list = [self.order_ttl_bg.text(), self.order_ttl_sea.text(), self.order_ttl_sld.text()]
        lbl_list = [order_lbl_bg, order_lbl_sea, order_lbl_sld]
        click_order.clicked.connect(lambda: TextFile(self, ttl_list, lbl_list))
        order_lay.addWidget(click_order)

        clearlist, order_lay_clear = AddLayWidget(["Side"])
        clear_ttl = LabelTitel("Избор Наново","Title",False)
        order_lay_clear.addWidget(clear_ttl)

        self.clearTabs = QButtonGroup()
        titles = ["Българска Кухня","Морска Кухня","Салатен Бар","Празен Списък"]
        clear_inlay = MenuRadBox(True,titles,self.clearTabs)

        clear_inlist = QWidget()
        clear_inlist.setObjectName("TabOra")
        clear_inlist.setLayout(clear_inlay)
        order_lay_clear.addWidget(clear_inlist)

        click_clear = QPushButton("Изтрий")
        click_clear.clicked.connect(lambda: self.ClearOut(order_lbl_bg,order_lbl_sea,order_lbl_sld))
        order_lay_clear.addWidget(click_clear)

        order_main.addWidget(clearlist)
        order_main.addStretch()


#       Меню
        main_tab = QTabWidget()
        main_tab.addTab(bg_tab,"Българска Кухня")
        main_tab.addTab(sea_tab,"Морска Кухня")
        main_tab.addTab(salad_tab,"Салатен Бар")

        frame = QGridLayout()
        frame.addWidget(main_tab,0,0)
        frame.addWidget(order_tab,0,1)
        self.setLayout(frame)


#   Функции
    def ClearOut(self,order_lbl_bg,order_lbl_sea,order_lbl_sld):
        collect = ""
        for x in self.clearTabs.buttons():
            if x.isChecked():
                collect = x.text()
                break

        if collect == "Българска Кухня":
            self.bg_collect = ClearRadArea(self, [order_lbl_bg])

        elif collect == "Морска Кухня":
            self.sea_collect = ClearRadArea(self, [order_lbl_sea])

        elif collect == "Салатен Бар":
            self.salad_collect = ClearRadArea(self, [order_lbl_sld])

        elif collect == "Празен Списък":
            boxset = [order_lbl_bg, order_lbl_sea, order_lbl_sld]
            self.bg_collect, self.sea_collect, self.salad_collect = ClearRadArea(self, boxset)

        else:
            QMessageBox.information(self, "Грешка", "Не е избрана опция за изтриване!", QMessageBox.Ok, QMessageBox.Ok)


    def MakeButtons(self,lay,food,order_lbl):

        multi = QPushButton("Избери Още")
        multi.clicked.connect(lambda: MealChoice(food, True))
        single = QPushButton("Един Избор")
        single.clicked.connect(lambda: MealChoice(food, False))
        order = QPushButton("Запиши Избор")
        order.clicked.connect(lambda: AddtoOrder(lay, food, order_lbl))

        return multi,single,order


if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(order_style)
    window = Ordering()
    window.setMaximumWidth(400)
    window.setMaximumHeight(800)
    sys.exit(app.exec_())