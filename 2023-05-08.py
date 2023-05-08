
ChatGPT
以下は、前回のコードに、決定ボタンがクリックされたときに新しいウィンドウを開くようにした例です。

python
Copy code
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QApplication, QDialog, QLabel

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
        dialog = QDialog(self)
        dialog_layout = QVBoxLayout(dialog)
        dialog_label = QLabel('新しいウィンドウです', dialog)
        dialog_layout.addWidget(dialog_label)
        dialog.exec_()
        
if __name__ == '__main__':
    app = QApplication([])
    widget = DecisionWidget()
    widget.show()
    app.exec_()
このクラスは、DecisionWidgetという名前で定義されています。initUIメソッドで、QPushButtonを作成し、決定ボタンがクリックされたときの処理を行うon_decision_clickedメソッドを定義しています。また、レイアウトを設定することで、決定ボタンをウィジェットの中央に配置しています。

on_decision_clickedメソッドでは、新しいダイアログを作成し、その中にQLabelを配置しています。QDialog.exec_()メソッドを呼び出すことで、ダイアログを表示し、メインウィンドウをブロックしています。

注意点として、新しいウィンドウを開くためには、QDialogを使用する必要があります。QDialogは、親ウィンドウに対してモーダルなダイアログを作成するために使用されます。

-----
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
