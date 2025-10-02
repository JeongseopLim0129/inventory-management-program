from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon
from db_helper import DB, DB_CONFIG

class add_fruit_window(QDialog):
    def __init__(self):
        super().__init__()
        self.db = DB(**DB_CONFIG)

        self.setWindowTitle("과일 추가")
        self.setWindowIcon(QIcon('icon-kiwi.png'))
        self.setGeometry(300, 300, 300, 200)

        layout = QHBoxLayout()

        self.input_name = QLineEdit()
        self.input_price = QLineEdit()
        self.input_amount = QLineEdit()
        self.btn_add = QPushButton("추가")
        self.btn_add.clicked.connect(self.add_fruit)

        layout.addWidget(QLabel("이름"))
        layout.addWidget(self.input_name)
        layout.addWidget(QLabel("가격"))
        layout.addWidget(self.input_price)
        layout.addWidget(QLabel("재고량"))
        layout.addWidget(self.input_amount)
        layout.addWidget(self.btn_add)
        self.setLayout(layout)

    def add_fruit(self):
        name = self.input_name.text().strip()
        price = self.input_price.text().strip()
        amount = self.input_amount.text().strip()
        if not name or not price or not amount:
            QMessageBox.warning(self, '오류', '과일 이름, 가격, 재고량을 모두 입력하세요')
            return            
        ok = self.db.insert_fruit(name, price, amount)
        if ok:
            QMessageBox.information(self, '완료', '추가되었습니다')
            self.input_name.clear()
            self.input_price.clear()
            self.input_amount.clear()
            self.accept()
            self.accepted.emit() # 메인 창에 업데이트를 알림
        else:
            QMessageBox.critical(self, '실패', '추가중 오류가 발생했습니다')