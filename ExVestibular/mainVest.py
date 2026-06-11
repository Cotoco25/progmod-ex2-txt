# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:38:25 2026

@author: PC42
"""

#arq = open("resultadosvestibular2025.txt", "r")

#def criaListaMaioresNotas(arquivo):
#    lista = []
#    for linha in arq:
#        listaNova = []
#        linha = linha.split(";")
#        nomeCurso = linha.strip()
#        qtdAl = int((arq.readline().strip())*2)
#        maiorNota = 0
#        listaNome = []
#        for i in range(qtdAl):
#            nome = arq.readline()
#            nota = arq.redline()
#            if nota>maiorNota:
#                maiorNota = nota
#                listaNome.append(nome)
#            return (maiorNota, listaNome)
#        listaNova.append(nomeCurso, maiorNota, listaNome)
#        lista.append(listaNova)
#    print(lista)

#print(criaListaMaioresNotas(arq))

def criaListaMaioresNotas():
    arq = open("resultadosvestibular2025.txt", "r")
    for linha in arq:
        linha = linha.strip()
        lst = linha.split(";")
        curso = lst[0]