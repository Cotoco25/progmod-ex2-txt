# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

arq = open("notasdisciplina.txt", "r")

for linha in arq: #linha recebe a proxima linha nao lida no arquivo
    codTurma = linha.strip()
    qtdAl = int(arq.readline().strip())
    total = 0
    for i in range(qtdAl):
        total += float(arq.readline().strip())
    med = total/qtdAl
    print(codTurma, med)

arq.close()