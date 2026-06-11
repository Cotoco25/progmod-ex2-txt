# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:09:55 2024

@author: Ferlin
"""
def carrega_cat1():
    arqE=open('categorias_filmes1.txt', 'r')
    l= arqE.read().strip().split('\n')
    for (i,el) in enumerate(l):
        l[i]=[el,0]
    arqE.close()
    print(l)
    return l
def carrega_cat2():
    arqE=open('categorias_filmes1.txt', 'r')
    l= []
    for linha in arqE:
        cat=linha.strip()
        l.append([cat,0])
    arqE.close()
    print(l)
    return l
def busca(lEstr,val):
    for (i,el) in enumerate(lEstr):
        if val == el[0]:
            return i
    return None

arqE= open('avaliacoes_filmes_completo.txt', 'r') 
lCont=carrega_cat1()
for linha in arqE:
    dados = linha.strip().split(',')
    categoria= dados[4]    
    pos= busca(lCont,categoria)   
    if pos !=None:
        lCont[pos][1]+=1
    

for el in lCont:
    print(f"{el[0]:10s}: {el[1]} filmes")