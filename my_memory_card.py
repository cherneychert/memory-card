#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGroupBox,
QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    rbg.hide()
    ans_group.show()
    btn.setText('Следующий вопрос')

def show_question():
    ans_group.hide()
    rbg.show()
    btn.setText('Ответить')
    button_group.setExclusive(False)
    rbn1.setChecked(False)
    rbn2.setChecked(False)
    rbn3.setChecked(False)
    rbn4.setChecked(False)
    button_group.setExclusive(True)

# def start_test():
#     if btn.text() == 'Ответить':
#         show_result()
#     else:
#         show_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_ans.setText(q.right_ans)
    show_question()

def show_correct(res):
    lb_res.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        mw.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    print(f'Статистика:\n-Количество вопросов: {mw.total}\n-Количество правильных ответов: {mw.score}\n-Рейтинг: {mw.score/mw.total*100} %')
    

def next_question():
    elem_list = randint(0, len(list_question)-1)
    ask(list_question[elem_list])
    mw.total += 1

def click_OK():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()


list_question = []
list_question.append(Question('какие негры самые вкусные ', 'черные', 'белые', 'коричневые', 'зеленый'))
list_question.append(Question('какого цвета негры', 'черные', 'белые ', 'зеленые','коричневая'))
list_question.append(Question('что курит автор опроса', 'пар зимой', 'сдобные соленые палочки', 'травку', 'сигареты'))
list_question.append(Question('комп в школе взорвется', 'когда включится', 'когда ты откроешь вкладку', 'когда вкладок будет больше одной', 'ниогда'))
list_question.append(Question('Какое самое толстое дерево на Земле?', 'черное', 'дуб', 'береза', 'ель'))
list_question.append(Question('Как называют жанр фильмов, который пугает зрителей?', 'фильм про негров', 'фентази', 'олег', 'про белых'))
list_question.append(Question('сколько членов в многочлене','много', '3 ', '4', '2'))
list_question.append(Question('Какой пульс у человека считается нормальным?','1488', '30 ', '40', '20'))







mem_card = QApplication([])
mw = QWidget()
mw.setWindowTitle('Memory card')
mw.resize(400, 350)

mw.total = 0
mw.score = 0

question = QLabel('Здесь будет вопрос')
btn = QPushButton('Ответить')

btn.clicked.connect(click_OK)
# Создание группы вопроса
rbg = QGroupBox('Варианты ответа')
rbn1 = QRadioButton('ответ 1')
rbn2 = QRadioButton('ответ 2')
rbn3 = QRadioButton('ответ 3')
rbn4 = QRadioButton('ответ 4')

answers = [rbn1, rbn2, rbn3, rbn4]

button_group = QButtonGroup()
button_group.addButton(rbn1)
button_group.addButton(rbn2)
button_group.addButton(rbn3)
button_group.addButton(rbn4)

layout_rbn12 = QHBoxLayout()
layout_rbn12.addWidget(rbn1)
layout_rbn12.addWidget(rbn2)
layout_rbn34 = QHBoxLayout()
layout_rbn34.addWidget(rbn3)
layout_rbn34.addWidget(rbn4)

layout_gr = QVBoxLayout()
layout_gr.addLayout(layout_rbn12)
layout_gr.addLayout(layout_rbn34)

rbg.setLayout(layout_gr)

#Создание группы ответа
ans_group = QGroupBox('Результаты теста') 
lb_res = QLabel('Правильно/Неправильно') 
lb_ans = QLabel('Правильны ответ здесь') 

ans_layout = QVBoxLayout()
ans_layout.addWidget(lb_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
ans_layout.addWidget(lb_ans, alignment=Qt.AlignCenter, stretch=2)

ans_group.setLayout(ans_layout)


layout1 = QHBoxLayout()# под вопрос(question)
layout2 = QHBoxLayout()# под группу(rbg)
layout3 = QHBoxLayout()# под кнопку(btn)

layout1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout2.addWidget(rbg)
ans_group.hide()
layout2.addWidget(ans_group)

layout3.addStretch(1)
layout3.addWidget(btn, stretch=2)
layout3.addStretch(1)

layout_mw = QVBoxLayout()
layout_mw.addLayout(layout1, stretch=2)
layout_mw.addLayout(layout2, stretch=8)
layout_mw.addStretch(1)
layout_mw.addLayout(layout3, stretch=1)
layout_mw.addStretch(1)
layout_mw.setSpacing(5)

next_question()
mw.setLayout(layout_mw)

mw.show()

mem_card.exec_()