# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:27:04 2026

@author: PC42
"""

arq = open("dadospessoas.txt", "r")

lista_rato = []
for i in range(9):
    lista_rato.append(1924 + 12*i)

lista_boi = []
for i in range(9):
    lista_rato.append(1925 + 12*i)

lista_tigre = []
for i in range(9):
    lista_tigre.append(1926 + 12*i)

lista_coelho = []
for i in range(9):
    lista_coelho.append(1927 + 12*i)

lista_dragao = []
for i in range(9):
    lista_dragao.append(1928 + 12*i)

lista_cobra = []
for i in range(9):
    lista_cobra.append(1929 + 12*i)

lista_cavalo = []
for i in range(9):
    lista_cavalo.append(1930 + 12*i)

lista_carneiro = []
for i in range(9):
    lista_carneiro.append(1931 + 12*i)

lista_macaco = []
for i in range(9):
    lista_macaco.append(1932 + 12*i)

lista_galo = []
for i in range(9):
    lista_galo.append(1933 + 12*i)

lista_cao = []
for i in range(9):
    lista_cao.append(1934 + 12*i)
    
lista_porco = []
for i in range(9):
    lista_porco.append(1935 + 12*i)
contRato = 0
for linha in arq:
    linha = linha.strip()
    lst = linha.split(";")
    signo = lst[1]
    signo = linha.split("/")
    signoFinal = signo[2]
    if signo[2] in lista_rato or signo[2] in lista_boi or signo[2] in lista_dragao:
        contRato += 1
        print(contRato)