from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QGridLayout, \
        QPushButton, QButtonGroup, QGroupBox, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
import sys


from menufiles.OrderCss import order_style
from menufiles.OrderLabels import LabelTitel
from menufiles.TabTitle import SetSectionTitel
from menufiles.AddItems import AddtoOrder
from menufiles.MenuImage import LoadImage
from menufiles.MakeChoice import MealChoice
from menufiles.DishesBox import MenuRadBox
from menufiles.LayWidget import AddLayWidget
from menufiles.ClearText import ClearRadArea
from menufiles.FileUpdate import TextFile


class Ordering(QWidget):
    def __init__(self):
        super().__init__()
        self.OrderMenu()


    def OrderMenu(self):
        self.setGeometry(50,50,400,800)
        self.setWindowIcon(QIcon("foodmenu/foodicon.png"))
        self.setWindowTitle("Choose a Dish and Order it")
        self.MenuItems()
        self.show()


    def MenuItems(self):
#       OrderTab Part1
        order_tab, order_main = AddLayWidget(["TabRed"])
        order_tab_sm, order_list = AddLayWidget(["TabOra"])
        mylist, order_lay = AddLayWidget(["Side"])
        order_main.addWidget(mylist)

        self.order_ttl_bg, order_lbl_bg = LabelTitel("Bulgarian Kitchen", "SmTitle", order_list)
        self.order_ttl_sea, order_lbl_sea = LabelTitel("Seaside Dishes", "SmTitle", order_list)
        self.order_ttl_sld, order_lbl_sld = LabelTitel("Salad Bar", "SmTitle", order_list)


#       Български Ястия
        bg_tab, bg_lay = AddLayWidget(["TabRed"])
        bg_food = ["wine kebab", "chicken spindle", "mixed grill", "royal casserole", "liver tinsel", "lamb fillet"]
        bg_food_veg = ["stuffed peppers", "mushroom plate", "breaded cheese", "potato gratin"]
        bg_meatfood = QButtonGroup()

        bg_lay_food = MenuRadBox(False, bg_food, bg_meatfood)
        bg_lay_veg = MenuRadBox(False, bg_food_veg, bg_meatfood)

        bg_text = "Traditional dishes from all over Bulgaria"
        bg_desc = SetSectionTitel("Bulgarian Kitchen",bg_text)
        bg_lay.addWidget(bg_desc)

        bg_food_pic = "foodmenu/bg-food.png"
        LoadImage(self, bg_food_pic, bg_lay)

        bg_meatbox = QGroupBox("Meat Dishes")
        bg_vegbox = QGroupBox("Meatless Dishes")

        AddLayWidget([bg_lay, [bg_meatbox, bg_vegbox]])
        bg_meatbox.setLayout(bg_lay_food)
        bg_vegbox.setLayout(bg_lay_veg)

        bg_bttns = QHBoxLayout()
        bg_multi,bg_single,bg_order = self.MakeButtons(self, bg_meatfood, order_lbl_bg)

        AddLayWidget([bg_bttns,[bg_multi,bg_single,bg_order]])
        bg_lay.addLayout(bg_bttns)
        bg_lay.addStretch()


#       Seaside Dishes
        sea_tab, sea_lay = AddLayWidget(["TabRed"])
        sea_food = ["surmullet", "bassfish", "herring", "tsatsa", "knobfish", "turbot"]
        sea_food_veg = ["squids", "shrimps", "mussels", "crabs"]
        sea_meatfood = QButtonGroup()

        sea_layfish = MenuRadBox(False, sea_food, sea_meatfood)
        sea_vegfish = MenuRadBox(False, sea_food_veg, sea_meatfood)

        sea_text = "Favorite dishes of fishermen and sailors in Bulgaria"
        sea_desc = SetSectionTitel("Seaside Dishes", sea_text)
        sea_lay.addWidget(sea_desc)

        seapic = "foodmenu/sea-food.png"
        LoadImage(self, seapic, sea_lay)

        sea_box = QGroupBox("Fish Dishes")
        sea_vegbox = QGroupBox("Seafood Plates")

        AddLayWidget([sea_lay,[sea_box,sea_vegbox]])
        sea_box.setLayout(sea_layfish)
        sea_vegbox.setLayout(sea_vegfish)

        sea_bttns = QHBoxLayout()
        sea_multi, sea_single, sea_order = self.MakeButtons(self, sea_meatfood, order_lbl_sea)

        AddLayWidget([sea_bttns,[sea_multi,sea_single,sea_order]])
        sea_lay.addLayout(sea_bttns)
        sea_lay.addStretch()


#       Salad Bar
        salad_tab, salad_mainlay = AddLayWidget(["TabRed"])
        salads = ["shopska","snowflake","russian","monastery","shepherd","garden","royal pickle"]
        salad_food = QButtonGroup()

        salad_lay = MenuRadBox(False, salads, salad_food)
        salad_text = "Salads according to recipes of Bulgarian farmers"
        sld_desc = SetSectionTitel("Salad Bar", salad_text)
        salad_mainlay.addWidget(sld_desc)

        seapic = "foodmenu/salad.png"
        LoadImage(self, seapic, salad_mainlay)

        saladbox = QGroupBox("Add Garnish")
        saladbox.setLayout(salad_lay)
        salad_mainlay.addWidget(saladbox)

        sld_bttns = QHBoxLayout()
        salad_multi,salad_single,salad_order = self.MakeButtons(self, salad_food, order_lbl_sld)

        AddLayWidget([sld_bttns, [salad_multi,salad_single,salad_order]])
        salad_mainlay.addLayout(sld_bttns)
        salad_mainlay.addStretch()


#       OrderTab Part2
        order_ttl = LabelTitel("Your Choice","Title",False)
        order_lay.addWidget(order_ttl)

        order_lay.addWidget(order_tab_sm)
        order_lay.addStretch()

        click_order = QPushButton("Order Now")
        ttl_list = [self.order_ttl_bg.text(), self.order_ttl_sea.text(), self.order_ttl_sld.text()]
        lbl_list = [order_lbl_bg, order_lbl_sea, order_lbl_sld]
        click_order.clicked.connect(lambda: TextFile(self, ttl_list, lbl_list))
        order_lay.addWidget(click_order)

        clearlist, order_lay_clear = AddLayWidget(["Side"])
        clear_ttl = LabelTitel("Clear List","Title",False)
        order_lay_clear.addWidget(clear_ttl)

        self.clearTabs = QButtonGroup()
        titles = ["Bulgarian Kitchen","Seaside Dishes","Salad Bar","Empty List"]
        clear_inlay = MenuRadBox(True,titles,self.clearTabs)

        clear_inlist = QWidget()
        clear_inlist.setObjectName("TabOra")
        clear_inlist.setLayout(clear_inlay)
        order_lay_clear.addWidget(clear_inlist)

        click_clear = QPushButton("Delete")
        click_clear.clicked.connect(lambda: self.ClearOut(order_lbl_bg,order_lbl_sea,order_lbl_sld))
        order_lay_clear.addWidget(click_clear)

        order_main.addWidget(clearlist)
        order_main.addStretch()


#       Main Menu
        main_tab = QTabWidget()
        main_tab.addTab(bg_tab,"Bulgarian Kitchen")
        main_tab.addTab(sea_tab,"Seaside Dishes")
        main_tab.addTab(salad_tab,"Salad Bar")

        frame = QGridLayout()
        frame.addWidget(main_tab,0,0)
        frame.addWidget(order_tab,0,1)
        self.setLayout(frame)


#   Methods
    def ClearOut(self,order_lbl_bg,order_lbl_sea,order_lbl_sld):
        collect = ""
        for x in self.clearTabs.buttons():
            if x.isChecked():
                collect = x.text()
                break

        if collect == "Bulgarian Kitchen":
            self.bg_collect = ClearRadArea(self, [order_lbl_bg])

        elif collect == "Seaside Dishes":
            self.sea_collect = ClearRadArea(self, [order_lbl_sea])

        elif collect == "Salad Bar":
            self.salad_collect = ClearRadArea(self, [order_lbl_sld])

        elif collect == "Empty List":
            boxset = [order_lbl_bg, order_lbl_sea, order_lbl_sld]
            self.bg_collect, self.sea_collect, self.salad_collect = ClearRadArea(self, boxset)

        else:
            QMessageBox.information(self, "Error", "No deletion option set for clearing the list!", QMessageBox.Ok, QMessageBox.Ok)


    def MakeButtons(self,lay,food,order_lbl):

        multi = QPushButton("Multy Choice")
        multi.clicked.connect(lambda: MealChoice(food, True))
        single = QPushButton("Single Choice")
        single.clicked.connect(lambda: MealChoice(food, False))
        order = QPushButton("Add to Order")
        order.clicked.connect(lambda: AddtoOrder(lay, food, order_lbl))

        return multi,single,order


if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(order_style)
    window = Ordering()
    window.setMaximumWidth(400)
    window.setMaximumHeight(800)
    sys.exit(app.exec_())