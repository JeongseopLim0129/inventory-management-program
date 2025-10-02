from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from db_helper import DB, DB_CONFIG

class delete_fruit_window(QDialog):
    def __init__(self):
        super().__init__()
        self.db = DB(**DB_CONFIG)

        self.setWindowTitle("과일 삭제")
        self.setWindowIcon(QIcon('icon-apple.png'))

        vbox = QVBoxLayout()
        layout = QHBoxLayout()
    
        self.calender = QCalendarWidget(self)
        self.calender.setGridVisible(True)
        self.calender.clicked[QDate].connect(self.show_date_fruits)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['ID', '과일 이름', '가격', '재고량', '입고일'])
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)

        self.input_target_name = QLineEdit()
        self.btn_add = QPushButton("삭제")
        self.btn_add.clicked.connect(self.delete_fruit)

        layout.addWidget(QLabel("이름"))
        layout.addWidget(self.input_target_name)
        layout.addWidget(self.btn_add)

        self.setLayout(vbox)
        vbox.addWidget(self.calender)
        vbox.addWidget(self.table)
        vbox.addLayout(layout)

    def delete_fruit(self):
        target = self.input_target_name.text().strip()

        if not target:
            QMessageBox.warning(self, '오류', '삭제할 과일을 입력하세요.')
            return
        
        ok = self.db.delete_fruit(target)
        if ok:
            QMessageBox.information(self, '완료', '삭제되었습니다')
            self.input_target_name.clear()
            self.accepted.emit()
            self.accept()          
        else:
            QMessageBox.critical(self, '실패', '삭제중 오류가 발생했습니다')

    def show_date_fruits(self):
        sel_date = self.calender.selectedDate().toString(Qt.ISODate)
        rows = self.db.fetch_date_fruits(sel_date)
        self.table.setRowCount(len(rows))
        for r, (id, name, price, amount, date) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(id)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(str(price)))
            self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
            self.table.setItem(r, 4, QTableWidgetItem(str(date)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)