# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:09:55 2024

@author: Ferlin
"""


arqE= open('avaliacoes_filmes_completo.txt', 'r') 
arqS= open('filmes_notas_maximas.txt', 'w') 
for linha in arqE:
    dados = linha.strip().split(',')
    filme = dados[0]
    tecnico = int(dados[1])
    enredo= int(dados[2])
    personagens=int(dados[3])
    categoria= dados[4]
    anoLancamento= int(dados[5])
    
    if tecnico == 5 and  enredo==5 and personagens==5:
        print(f"{filme} = {categoria}  = {anoLancamento}")
        arqS.write(f"{filme},{categoria},{anoLancamento}\n")
arqE.close()
arqS.close()