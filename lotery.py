from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('Лотерея')
main_win.move(150,200)
main_win.resize(400,400)

button=QPushButton("Випробувати удачу")
text=QLabel("Натисни щоб взяти участь")
num1 = QLabel("?")
num2=QLabel("?")

line=QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(num1, alignment=Qt.AlignCenter)
line.addWidget(num2, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(line)
def show_num():
    rnum1=randint(1,10)
    rnum2=randint(1,10)
    num1.setText(str(rnum1))
    num2.setText(str(rnum2))
    if rnum1==rnum2:
        text.setText("Ви виграли! Зіграйте знову")
    else:
        text.setText("Ви програли! Зіграйте знову")
button.clicked.connect(show_num)
main_win.show()
app.exec_()