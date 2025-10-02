from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from db_helper import DB, DB_CONFIG

class delete_fruit_window(QDialog):
    def __init__(self):
        super().__init__()
        self.db = DB(**DB_CONFIG)

        self.setWindowTitle("과일 삭제")
        self.setWindowIcon(QIcon('icon-apple.png'))
        self.setGeometry(300, 300, 300, 200)

        layout = QHBoxLayout()

        self.input_target_name = QLineEdit()
        self.btn_add = QPushButton("삭제")
        self.btn_add.clicked.connect(self.delete_fruit)

        layout.addWidget(QLabel("이름"))
        layout.addWidget(self.input_target_name)
        layout.addWidget(self.btn_add)
        self.setLayout(layout)

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