from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QHBoxLayout, QTableWidget, QTableWidgetItem
from db_helper import DB, DB_CONFIG

class update_info_window(QDialog):
    def __init__(self):
        super().__init__()
        self.db = DB(**DB_CONFIG)

        self.setWindowTitle("정보 수정")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()
        search_box = QHBoxLayout()
        self.input_target_name = QLineEdit()
        self.btn_add0 = QPushButton("검색")
        self.btn_add0.clicked.connect(self.search_fruit)
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['ID', '과일 이름', '가격', '재고량'])
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        form_box = QHBoxLayout()
        self.input_name = QLineEdit()
        self.btn_add1 = QPushButton("이름 수정")
        self.btn_add1.clicked.connect(self.update_name_info)
        self.input_price = QLineEdit()
        self.btn_add2 = QPushButton("가격 수정")
        self.btn_add2.clicked.connect(self.update_price_info)
        self.input_amount = QLineEdit()
        self.btn_add3 = QPushButton("재고량 수정")
        self.btn_add3.clicked.connect(self.update_amount_info)

        search_box.addWidget(self.input_target_name)
        search_box.addWidget(self.btn_add0)

        form_box.addWidget(QLabel("이름"))
        form_box.addWidget(self.input_name)
        form_box.addWidget(self.btn_add1)
        form_box.addWidget(QLabel("가격"))
        form_box.addWidget(self.input_price)
        form_box.addWidget(self.btn_add2)
        form_box.addWidget(QLabel("재고량"))
        form_box.addWidget(self.input_amount)
        form_box.addWidget(self.btn_add3)
        
        layout.addLayout(search_box)
        layout.addWidget(self.table)
        layout.addLayout(form_box)
        self.setLayout(layout)

    def search_fruit(self):
        target = self.input_target_name.text().strip()
        if not target :
            QMessageBox.warning(self, '오류', '검색할 과일을 입력하세요')
            return
        
        ok = self.db.search_fruit_info(target)
        if ok:
            rows = self.db.search_fruit_info(target)
            self.table.setRowCount(len(rows))
            for r, (id, name, price, amount) in enumerate(rows):
                self.table.setItem(r, 0, QTableWidgetItem(str(id)))
                self.table.setItem(r, 1, QTableWidgetItem(name))
                self.table.setItem(r, 2, QTableWidgetItem(str(price)))
                self.table.setItem(r, 3, QTableWidgetItem(str(amount)))
            self.table.resizeColumnsToContents()          
        else:
            QMessageBox.critical(self, '실패', '검색 오류가 발생했습니다')

    def update_name_info(self):
        target = self.input_target_name.text().strip()
        new_name = self.input_name.text().strip()

        if not target:
            QMessageBox.warning(self, '오류', '수정할 과일을 먼저 검색하거나 입력하세요.')
            return
        
        if not new_name:
            QMessageBox.warning(self, '오류', '새로운 과일 이름을 입력하세요')
            return
        
        ok = self.db.update_name_info(new_name, target)
        if ok:
            QMessageBox.information(self, '완료', '수정되었습니다')
            self.input_name.clear()
            self.input_target_name.setText(new_name)
            self.search_fruit()           
        else:
            QMessageBox.critical(self, '실패', '수정중 오류가 발생했습니다')

    def update_price_info(self):
        target = self.input_target_name.text().strip()
        new_price = self.input_price.text().strip()

        if not target:
            QMessageBox.warning(self, '오류', '수정할 과일을 먼저 검색하거나 입력하세요.')
            return

        if not new_price:
            QMessageBox.warning(self, '오류', '새로운 가격을 입력하세요.')
            return
        
        ok = self.db.update_price_info(new_price, target)
        if ok:
            QMessageBox.information(self, '완료', '수정되었습니다')
            self.input_price.clear()
            self.search_fruit()           
        else:
            QMessageBox.critical(self, '실패', '수정중 오류가 발생했습니다')

    def update_amount_info(self):
        target = self.input_target_name.text().strip()
        new_amount = self.input_amount.text().strip()

        if not target:
            QMessageBox.warning(self, '오류', '수정할 과일을 먼저 검색하거나 입력하세요.')
            return
        
        if not new_amount:
            QMessageBox.warning(self, '오류', '새로운 재고량을 입력하세요')
            return
        
        ok = self.db.update_amount_info(new_amount, target)
        if ok:
            QMessageBox.information(self, '완료', '수정되었습니다')
            self.input_name.clear()
            self.input_price.clear()
            self.input_amount.clear()
            self.search_fruit()           
        else:
            QMessageBox.critical(self, '실패', '수정중 오류가 발생했습니다')
