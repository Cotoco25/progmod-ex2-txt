# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:09:55 2024

@author: Ferlin
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
    filme = dados[0]
    tecnico = int(dados[1])
    enredo= int(dados[2])
    personagens=int(dados[3])
    categoria= dados[4]
    anoLancamento= int(dados[5])
    media=(tecnico+enredo+personagens)/3
    
    if media >=4:
        pos= busca(lCont,anoLancamento)  
        if pos != None:
            lCont[pos][1]+=1
        else:
            lCont.append([anoLancamento,1])
    
lCont.sort()
for el in lCont:
    print(f"{el[0]}:{el[1]}")