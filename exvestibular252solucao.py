# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 15:08:53 2025

@author: joisa
"""
# No arquivo resultadosvestibular2025.txt há as informações 
# do vestibular de uma universidade com cursos almejados e 
# candidatos e suas respectivas notas  

# A estrutura do arquivo é:

# Para cada CURSO constam no arquivo:
# Linha com CURSO e qtd x de candidatos que desejam o curso (separados por ;)
# Seguida de x linhas com nome e nota do candidato (separados por ;) .

# A) Escreva uma função, criaListaMaioresNotas, que leia os dados do arquivo  
# e crie e retorne uma nova lista em que cada elemento é uma sublista
# com curso, maior nota no curso, lista de nomes com essa maior nota.

# Para o arquivo fornecido seria retornada a lista:
# [['MEDICINA', 8.2, ['DEDE']], ['MATEMATICA', 8.2, ['LULU', 'BUBA']], 
#   ['DIREITO', 9.5, ['NENO', 'NINA', 'KIKA']], ['ECONOMIA', 8.5, ['MINA']]]


# B) Escreva um função, exibeCursos, que receba uma lista com a estrutura 
# da lista retornada no item (A) e exiba curso, maior nota e alunos de maior 
# nota com o formato a seguir:
# ==== Curso:MEDICINA - Nota máxima:8.2 ===
# ---> DEDE

# ==== Curso:MATEMATICA - Nota máxima:8.2 ===
# ---> LULU
# ---> BUBA

# ==== Curso:DIREITO - Nota máxima:9.5 ===
# ---> NENO
# ---> NINA
# ---> KIKA

# ==== Curso:ECONOMIA - Nota máxima:8.5 ===
# ---> MINA 
    
    
# Assuma q não há curso com 0 alunos

# ATENÇÃO: tem que funcionar para qualquer outro arquivo
# com a mesma estrutura


#A)
def criaListaMaioresNotas():
    lcursos=[]
    
    arq= open('resultadosvestibular2025.txt','r')
    
    for linha in arq:
        linha= linha.strip()
        lst= linha.split(';')
        curso=lst[0]
        qtd= int(lst[1])
        maiorNotaDoCurso=0
        lMaioresDoCurso=[]
        for i in range(qtd):
            linhaAl= arq.readline()
            lstAl= linhaAl.strip().split(';')
            nomeAl= lstAl[0]
            nota= float(lstAl[1])
            if nota == maiorNotaDoCurso:
                lMaioresDoCurso.append(nomeAl)
            elif nota > maiorNotaDoCurso:
                maiorNotaDoCurso = nota 
                lMaioresDoCurso=[nomeAl]
        lcursos.append([curso,maiorNotaDoCurso,lMaioresDoCurso])
    arq.close()
    return lcursos

#B)

def exibeCursos(lcurso):
    for el in lcurso:
        print(f'\n==== Curso:{el[0]} - Nota máxima:{el[1]} ===')
        for alu in el[2]:
            print(f'---> {alu}')

#BP
listaDeCursos= criaListaMaioresNotas()
#print(l)
exibeCursos(listaDeCursos)
                

