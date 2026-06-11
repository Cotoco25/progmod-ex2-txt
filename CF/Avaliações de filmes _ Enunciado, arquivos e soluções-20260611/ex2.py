# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:09:55 2024

@author: Ferlin
"""

# Carregar o arquivo "avaliacoes_filmes_com_ano.txt" e estruturar os dados


arqE= open('avaliacoes_filmes_completo.txt', 'r') 
lCont=[0]*5
for linha in arqE:
    dados = linha.strip().split(',')
    filme = dados[0]
    tecnico = int(dados[1])
        
    lCont[tecnico-1]+=1

for (i,el) in enumerate(lCont):
    print(f" Nota {i+1}: {el} filmes")