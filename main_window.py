from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton, QMessageBox, QDialog
from db_helper import DB, DB_CONFIG
from add_fruit_window import add_fruit_window
from update_info_window import update_info_window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DB(**DB_CONFIG)
        self.setWindowTitle('과일 재고 관리')

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        form_box = QHBoxLayout()
        self.btn_add1 = QPushButton('새로운 과일 추가')
        self.btn_add1.clicked.connect(self.open_add_fruit_window)
        self.btn_add2 = QPushButton('정보 수정')
        self.btn_add2.clicked.connect(self.open_update_info_window)
        
        sort_box = QHBoxLayout()
        self.btn_add3 = QPushButton('이름순')
        self.btn_add3.clicked.connect(self.sort_by_name)
        self.btn_add4 = QPushButton('상품번호순')
        self.btn_add4.clicked.connect(self.sort_by_id)
        sort_box.addWidget(self.btn_add3)
        sort_box.addWidget(self.btn_add4)

        form_box.addWidget(self.btn_add1)
        form_box.addWidget(self.btn_add2)
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

    def open_add_fruit_window(self):
        self.add_dialog = add_fruit_window()
        self.add_dialog.accepted.connect(self.load_fruits)
        self.add_dialog.exec_()

    def open_update_info_window(self):
        self.add_dialog = update_info_window()
        self.add_dialog.accepted.connect(self.load_fruits)
        self.add_dialog.exec_()

    def sort_by_name(self):
        rows = self.db.fetch_fruits_order_by_name()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()

    def sort_by_id(self):
        rows = self.db.fetch_fruits()
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
        self.table.resizeColumnsToContents()