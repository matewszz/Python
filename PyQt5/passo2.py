#Criando os botões de comando#

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        botao1 = QPushButton('Botão 1', self)
        botao1.move(100, 150)
        botao1.resize(150, 150)
        botao1.setStyleSheet('QPushButton {background-color: #ADD8E6}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(300, 150)
        botao2.resize(150, 150)
        botao2.setStyleSheet('QPushButton {background-color: #87dc8d}')
        botao2.clicked.connect(self.botao2_click)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.largura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click (self):
        print("Botão1 selecionado!")

    def botao2_click (self):
        print('Botão2 selecionado!')

aplicacao = QApplication(sys.argv)
j = janela()
sys.exit(aplicacao.exec_())
