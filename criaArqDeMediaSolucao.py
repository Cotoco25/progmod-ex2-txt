# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

# Escreva um programa que a partir dos 
# dados do arquivo notasdisciplina.txt
# crie um arq, mediasturmas.txt, com 
# em que cada linha tenha turma e média
# da turma (com 1 casa decimal), separadas 
# por ,

# Em notasdisciplina.txt temos as seguintes
# informações (uma por linha):
# TURMA
# QTD alunos da turma
# Nota1 da turma
# Nota2 da turma
# ...

# Isso se repete para todas as turmas.

arq = open('notasdisciplina.txt','r')
saida= open('mediasturmas.txt','w')
for linha in arq:
    turma= linha.strip()
    qtdAl= int(arq.readline().strip())
    tot=0.0
    for i in range(qtdAl):
        tot+= float(arq.readline().strip())
    med= tot/qtdAl
    print(f'{turma},{med:.1f}')
    saida.write(f'{turma},{med:.1f}\n')

arq.close()
saida.close()






