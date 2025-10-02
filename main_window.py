from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from db_helper import DB, DB_CONFIG
from add_fruit_window import add_fruit_window
from update_info_window import update_info_window
from delete_fruit_window import delete_fruit_window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DB(**DB_CONFIG)
        self.setWindowTitle('과일 재고 관리')

        central = QWidget()
        self.setCentralWidget(central)
        self.setWindowIcon(QIcon('icon-basket.png'))
        vbox = QVBoxLayout(central)

        form_box = QHBoxLayout()
        
        self.btn_add1 = QPushButton('새로운 과일 추가')
        self.btn_add1.setStyleSheet("color: black;"
                      "background-color: #3FE87F;"
                      "border-style: solid;"
                      "border-width: 2px;"
                      "border-color: #3FE87F;"
                      "border-radius: 3px")
        self.btn_add1.clicked.connect(self.open_add_fruit_window)
        self.btn_add2 = QPushButton('과일 정보 수정')
        self.btn_add2.setStyleSheet("color: black;"
                      "background-color: #F0E969;"
                      "border-style: solid;"
                      "border-width: 2px;"
                      "border-color: #F0E969;"
                      "border-radius: 3px")
        self.btn_add2.clicked.connect(self.open_update_info_window)
        self.btn_add5 = QPushButton('과일 삭제')
        self.btn_add5.setStyleSheet("color: black;"
                      "background-color: #F05650;"
                      "border-style: solid;"
                      "border-width: 2px;"
                      "border-color: #F05650;"
                      "border-radius: 3px")
        self.btn_add5.clicked.connect(self.open_delete_fruit_window)
        
        sort_box = QHBoxLayout()
        self.btn_add3 = QPushButton('이름순')
        self.btn_add3.clicked.connect(self.sort_by_name)
        self.btn_add4 = QPushButton('상품번호 ↑')
        self.btn_add4.clicked.connect(self.sort_by_id)
        self.btn_add10 = QPushButton('상품번호 ↓')
        self.btn_add10.clicked.connect(self.sort_by_id_rev)
        self.btn_add6 = QPushButton('가격 ↑')
        self.btn_add6.clicked.connect(self.sort_by_price)
        self.btn_add7 = QPushButton('가격 ↓')
        self.btn_add7.clicked.connect(self.sort_by_price_rev)
        self.btn_add8 = QPushButton('재고 ↑')
        self.btn_add8.clicked.connect(self.sort_by_amount)
        self.btn_add9 = QPushButton('재고 ↓')
        self.btn_add9.clicked.connect(self.sort_by_amount_rev)
        sort_box.addWidget(self.btn_add3)
        sort_box.addWidget(self.btn_add4)
        sort_box.addWidget(self.btn_add10)
        sort_box.addWidget(self.btn_add6)
        sort_box.addWidget(self.btn_add7)
        sort_box.addWidget(self.btn_add8)
        sort_box.addWidget(self.btn_add9)

        form_box.addWidget(self.btn_add1)
        form_box.addWidget(self.btn_add2)
        form_box.addWidget(self.btn_add5)
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['ID', '과일 이름', '가격', '재고량'])
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)

        vbox.addLayout(sort_box)
        vbox.addWidget(self.table)
        vbox.addLayout(form_box)
        
        self.load_fruits()

    def load_fruits(self):
        rows = self.db.fetch_fruits()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def open_add_fruit_window(self):
        self.add_dialog = add_fruit_window()
        self.add_dialog.accepted.connect(self.load_fruits)
        self.add_dialog.exec_()

    def open_update_info_window(self):
        self.update_dialog = update_info_window()
        self.update_dialog.accepted.connect(self.load_fruits)
        self.update_dialog.exec_()

    def open_delete_fruit_window(self):
        self.del_dialog = delete_fruit_window()
        self.del_dialog.accepted.connect(self.load_fruits)
        self.del_dialog.exec_()

    def sort_by_name(self):
        rows = self.db.fetch_fruits_order_by_name()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def sort_by_price(self):
        rows = self.db.fetch_fruits_order_by_price()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def sort_by_price_rev(self):
        rows = self.db.fetch_fruits_order_by_price_rev()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def sort_by_amount(self):
        rows = self.db.fetch_fruits_order_by_amount()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def sort_by_amount_rev(self):
        rows = self.db.fetch_fruits_order_by_amount_rev()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def sort_by_id(self):
        rows = self.db.fetch_fruits()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def sort_by_id_rev(self):
        rows = self.db.fetch_fruits_rev()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)