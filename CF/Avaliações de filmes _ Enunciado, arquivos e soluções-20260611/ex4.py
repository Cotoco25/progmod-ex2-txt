# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:09:55 2024

@author: Ferlin
"""
def carrega_cat():
   
    arqE=open('categorias_filmes.txt', 'r')
    l= arqE.read().strip().split('\n')
    for (i,el) in enumerate(l):
        l[i]=[el,[]]
    arqE.close()
   
    return l

def busca(lEstr,val):
    for (i,el) in enumerate(lEstr):
        if val == el[0]:
            return i
    return None

arqE= open('avaliacoes_filmes_completo.txt', 'r') 
lGrupos=carrega_cat()
for linha in arqE:
    dados = linha.strip().split(',')
    filme= dados[0] 
    categoria= dados[4]    
    pos= busca(lGrupos,categoria)  
    if pos != None:
        lGrupos[pos][1].append(filme)
    

for el in lGrupos:
    print(f"{el[0]}:\n\t{el[1]}")