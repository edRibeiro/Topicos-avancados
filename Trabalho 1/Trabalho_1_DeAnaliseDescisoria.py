# Das opisoes de lazer abaixo, qual voce faria no sru fian de semana?
# Ir ao cinema, Assistir uma peça de teatro, Passear de Bicicleta,
# Visitar um museu, Jogar paintball, Ir a um parque aquático,
# Ir ao karaokê, Jogar boliche

#Início do Programa
# 'Qual atividade voce faria neste final de semana?'
# 1 - Ir ao cinema;
# 2 - Assistir uma peça de teatro;
# 3 - Passear de Bicicleta;
# 4 - Visitar um museu;
# 5 - Jogar paintball;
# 6 - Ir a um parque aquático;
# 7 - Ir ao karaokê;
# 8 - Jogar boliche;

import random
import math
def somatorio(n): # aqui definimos a funcao fatorial
   if n<=1: # se n for menor ou igual a um fatorial e 1
      return 1
   else: # caso contrario
      return n+somatorio(n-1)
       
def transposta(M):
    aux=[]
    for j in range(len(M[0])):
        linha=[]
        for i in range(len(M)):
            linha.append(M[i][j])
        aux.append(linha)
    return aux

def media(M):
    total=[]
    for linha in range(len(M)):
        soma=0
        for col in range(len(M[linha])):
            soma += M[linha][col]
        total.append(soma/len(M[linha]))
    return total

def windson(M):
    total=[]
    for linha in range(len(M)):
        l=M[linha][:]
        l.sort(reverse=True)
        mn=min(l)
        #print(mn)
        mx=max(l)
        #print(mx)
        #print(l)
        while (mx in l):
           l.remove(mx)
        while (mn in l):
           l.remove(mn)
        
        soma=0
        #print(l)
        for col in range(len(l)):
            soma += l[col]
        total.append(soma/len(M[linha]))
        #print('ALT[%d]'% (linha+1),' :: ',"%.2f" %  total[linha])
    return total

def ponderada(M):
    totalpesos=[]    
    somadivisor= somatorio(8)
    for linha in range(len(M)):
        pesos=[0,0,0,0,0,0,0,0]
        for col in range(len(M[linha])):
            if M[linha][col]==1:
               pesos[0]+=1
            elif M[linha][col]==2:
               pesos[1]+=1
            elif M[linha][col]==3:
               pesos[2]+=1
            elif M[linha][col]==4:
               pesos[3]+=1
            elif M[linha][col]==5:
               pesos[4]+=1
            elif M[linha][col]==6:
               pesos[5]+=1
            elif M[linha][col]==7:
               pesos[6]+=1
            else:
               pesos[7]+=1
        somadividendo=0
        for col in range(len(pesos)):
            somadividendo+=(col+1)*pesos[col]
        totalpesos.append(somadividendo/somadivisor)
    return totalpesos
            
def tng(M):
    total=[]
    for linha in range(len(M)):
        soma=0
        for col in range(len(M[linha])):
            soma += M[linha][col]
        total.append(soma)
    return total   

def mostrarmedia(m,n):
    for i in range(len(m)):
        print(n[i],' - média: ',"%.2f" %  m[i])

def mostrarTNG(m,n):
    for i in range(len(m)):
        print(n[i],' - Total: ',m[i])

def mostrarResultado(m,n):
    for i in range(len(m)):
        print(n[i],' :: ',"%.2f" %  m[i])
def resultado(M, alt):
   resut={}
   MEDIA=media(M)
   MPONDERADA=ponderada(M)
   TNG=tng(M)
   WINDISON=windson(M)
   #try:
   for i in range(len(M)):
      resut[alt[i]]=[M[i], WINDISON[i], MEDIA[i], MPONDERADA[i], TNG[i]]
   for chave, valor in resut.items():
      print(chave,'==>', valor)
   #except: 
      #print('Erro insperado')
   
alt=[
    'Ir ao cinema                 ',
    'Assistir uma peça de teatro  ',
    'Passear de Bicicleta         ',
    'Visitar um museu             ',
    'Jogar paintball              ',
    'Ir a um parque aquático      ',
    'Ir ao karaokê                ',
    'Jogar boliche                '
    ]
tabela = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
    ]
for linha in range(0, len(tabela)):
    itens=[1,2,3,4,5,6,7,8]
    random.shuffle(itens)
    tabela[linha]=itens

t=transposta(tabela)

for linha in range(0, len(t)):
   print(t[linha])
print('\n Média\n')
mostrarResultado(media(t), alt)
#print('')
#ponderada(t)
print('\n TNG\n')
mostrarResultado(tng(t), alt)
print('\n Média Ponderada\n')
mostrarResultado(ponderada(t),alt)
print('\n Média de Windson\n')
mostrarResultado(windson(t),alt)
print('\n\n')
#resultado(t,alt)




