from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QApplication

class DecisionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        # 決定ボタンを作成
        self.decision_button = QPushButton('決定', self)
        self.decision_button.clicked.connect(self.on_decision_clicked)
        
        # レイアウトを設定
        layout = QVBoxLayout(self)
        layout.addWidget(self.decision_button)
        
    def on_decision_clicked(self):
        # 決定ボタンがクリックされたときの処理
        print('決定ボタンがクリックされました')
        
if __name__ == '__main__':
    app = QApplication([])
    widget = DecisionWidget()
    widget.show()
    app.exec_()
