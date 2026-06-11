# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:09:55 2024

@author: Ferlin

Construa um programa que leia o arquivo 
avaliacoes_filmes_completo.txt calcule e mostre a 
quantidade de filmes em cada categoria existente no arquivo 
avaliacoes_filmes_completo
"""
def busca(lEstr,val):
    for (i,el) in enumerate(lEstr):
        if val == el[0]:
            return i
    return None

arqE= open('avaliacoes_filmes_completo.txt', 'r') 
lCont=[]
for linha in arqE:
    dados = linha.strip().split(',')
    categoria= dados[4]    
    pos= busca(lCont,categoria)   
    if pos !=None:
        lCont[pos][1]+=1
    else:
        lCont.append([categoria,1])
    

for el in lCont:
    print(f"{el[0]:10s}: {el[1]} filmes")