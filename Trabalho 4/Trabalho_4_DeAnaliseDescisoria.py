import math
from operator import itemgetter
def main():
    print ("    Topicos Avançados")
    print ("    Analise Descisoria\n")
    print ("    Trabalho: Método de Análise Hierárquica\n") 
    print ("Foco Principal: Escolha de um altomóvel")
    print ("Conjunto de alternativas viáveis:")
    alt=["Onix 1.0", "HB20 1.0", "Gol 1.0"]
    print (alt)
    print ("Conjunto de critérios:")
    crt=["Preço","Segurança","Consumo","Desempenho","Custo/Beneficio","Conforto","Estilo"]
    print (crt)
    print("\n")
    print ("Talbela de pagamentos\n      ", alt)

    tbl_pagamentos=[
        [36990,37995,39219],
        [8,8,7],
        [8,9,8],
        [7,9,8],
        [8,6,8],
        [9,8,7],
        [9,8,6]
        ]
    for i in range(len(tbl_pagamentos)):
        print(crt[i],": ",tbl_pagamentos[i])

    dp=[##Desenpenho das alternativas à luz de cada critério.
        [##1 - preço
            [1,4,7],
            [(1/4),1,4],
            [(1/7),(1/4),1]
        
        ],
        [##2 - segurança
            [1,1,3],
            [1,1,3],
            [1/3,1/3,1]
        ],
        [##3 - consumo
            [1,1/7,1],
            [7,1,7],
            [1,1/7,1]
        ],
        [##4 - desempenho
            [1,1/7,1/4],
            [7,1,3],
            [4,1/3,1]
        ],
        [##5 - beneficio
            [1,7,1],
            [1/7,1,1/7],
            [1,7,1]
        ],
        [##6 - conforto
            [1,5,7],
            [1/5,1,3],
            [1/7,1/3,1]
        ],
        [##7 - estilo
            [1,8,9],
            [1/8,1,5],
            [1/9,1/5,1]
        ]
    ]


    fp=[## Desempenho dos critérios à luz do foco principal.
        [1.0, 8.0, 1.0, 3.0, 1.0, 4.0, 9.0],
        [1/8, 1.0, 7.0, 7.0, 1/9, 3.0, 4.0],
        [1.0, 1/7, 1.0, 2.0, 1.0, 6.0, 8.0],
        [1/3, 1/7, 1/2, 1.0, 1/2, 6.0, 7.0],
        [1.0, 9.0, 1.0, 2.0, 1.0, 9.0, 9.0],
        [1/4, 1/3, 1/6, 1/6, 1/9, 1.0, 1/2],
        [1/9, 1/4, 1/8, 1/7, 1/9, 2.0, 1.0]
    ]
    print ("\nDesempenho dos criterios à luz do Foco Principal")
    print("Foco Peincipal ",crt)
    for i in range(len(fp)):
        print(crt[i]," ",fp[i])
    
    print ("\nDesempenho das alternativas à luz dos critérios")
    for i in range(len(dp)):
        print("\n",crt[i]," ",alt)
        for j in range(len(dp[i])):
            print (alt[j]," ",dp[i][j])
            
    norm = normalizar(dp)##Desempenho das alternativas, à luz critérios, normalizados
    print ("\nDesempenho das alternativas à luz dos critérios após serem normalizados")
    for i in range(len(norm)):
        for j in range(len(norm[i])):
            print("\n",crt[i]," ",alt)
            for k in range(len(norm[i][j])):
                print (alt[k]," ",norm[i][j][k])
                
    normFP = normalizarFP(fp)##Desempenho dos criterios à luz do foco principal normalizado.
    print(normFP)
    print ("\nDesempenho dos criterios à luz do Foco peincipal após ser normalizado")
    print("\nFoco Principal ",crt)
    for k in range(len(normFP)):
        print (crt[k]," ",normFP[k])
    

    ##PRIORIDADES MÉDIAS LOCAIS
    print("\nPML's à luz dos criterios.\n")
    pml=[]##Vetor de prioridades médias locais
    for i in range(len(norm)):
        pml.append(calcularPML(norm[i]))
        print("\n",crt[i],"=",pml[i])
    print("\nPML's à luz do Foco Principal.\n")
    pmlfp=calcularPMLFP(normFP)##Vetor de prioridades dos critérios à luz do Foco principal.
    for i in range(len(pmlfp)):
        print("\n",crt[i],"=",pmlfp[i])
    ##PRIORIDADES MÉDIAS GLOBAIS

    pg=calcularPG(pml,pmlfp)##Vetor de prioridades médias globais
    print("\n Desempenhos das alternativas à luz do Foco Principal")
    for i in range(len(pg)):
        print(alt[i],": ",round(pg[i],2))
    mostrarResultado(pg, alt)
    
    ##Análise de Consistência
    
    ic=inconsistencia(dp, pml)##Vetor dos Índices de Consistência
    print("\nÍndice da Consistência")
    for i in range(len(ic)):
        print(crt[i],"= ",ic[i])
    print("\nRazão de Consistência")
    rc=razaoConsistencia(ic, len(alt))##Vetor das Razões de Consistência
    for i in range(len(ic)):
        print(crt[i],"= ",rc[i])

    analise(rc, crt)
    
####################################################################
def analise(rc, crt):##função para análise segundo o metédo proposto por Saaty.
    fora=[]
    for i in range(len(rc)):
        if rc[i]>=0.1:
            fora.append(crt[rc.index(max(rc))])
    if len(fora)>0:
        print("\nTolerancia da Razão de Consistencia quebrada! Revisar modelo ou julgamentos.")
        print("Itens com inconsistencia ")
        for i in fora:
            print(" ",i)
    else:
        print("Nenhuma Razão de Consistencia fora do padrão.")

def mostrarResultado(pg, alt):
    print("\nO automovel que melhor atende ao as necessidades do decisor é o ", alt[pg.index(max(pg))],".")
    
def razaoConsistencia(ic, ordemDaMatriz):##Função para calcular a razão de consistência.
    icr=[## ÍNDICES DE CONSISTÊNCIA RANDÔMICOS
        0.00,##0
        0.00,##1
        0.00,##2
        0.58,##3
        0.90,
        1.12,
        1.24,
        1.32,
        1.41,
        1.45
        ]
    print("ICR=,", icr[ordemDaMatriz])
    rc=[]
    for i in range(len(ic)):
        rc.append(ic[i]/icr[ordemDaMatriz])
    return rc
    
def inconsistencia(dp, pml):##Função para calcular os índices de Consistência
    n=len(dp[0])
    ic=[]
    for i in range(len(dp)):
        ic.append(modulo(autovalores(dp[i][:], pml[i])-n)/(n-1))
    return ic

def autovalores(dp, pml):##Função que retorna o maior autovalor de um critério.
    dpaux=[]
    for i in range(len(dp)):
        col=[]
        for j in range(len(dp[i])):
            col.append(dp[i][j]*pml[j])
        dpaux.append(col)
    priaux=[]
    for i in range(len(dpaux)):
        priaux.append(somalinha(dpaux[i])/pml[i])
    lmax=somalinha(priaux)/len(priaux)
    return lmax

def calcularPG(pml,pmlfp):
    pg=[]
    soma=0
    linha=len(pml)
    col=len(pml[0])
    for i in range(col):
        soma=0
        for j in range(linha):
            soma+=pmlfp[j]*pml[j][i]
        pg.append(soma)
    return pg
            
    
def calcularPMLFP(dp):
    pml=[]
    for i in range(len(dp)):
        somalinha=0
        for j in range(len(dp[i])):
            somalinha+=round(dp[i][j],2)
        somalinha/=len(dp)
        pml.append(round(somalinha,2))
    return pml
        
def calcularPML(dp):
    pml=[]
    for i in range(len(dp[0])):
        somalinha=0
        for j in range(len(dp[0][i])):
            somalinha+=dp[0][i][j]
        somalinha/=len(dp[0][i])
        pml.append(somalinha)
    return pml
def normalizarFP(dp):
    scrt=[]
    norm=[]    
    for i in range(len(dp)):
        soma=0
        for j in range(len(dp[i])):
            soma+=dp[j][i]
        scrt.append(soma)
    for i in range(len(dp)):
        linha=[]
        for j in range(len(dp[i])):
            linha.append(round(dp[i][j]/scrt[j],2))
        norm.append(linha)
    return norm

def normalizar(dp):
    scrt=[]
    norm=[]
    for i in range(len(dp)):
        scrt.append(somacoluna(dp[i]))
    for i in range(len(dp)):
        norm.append(divCelulas(dp[i], scrt[i]))
    return norm
                
def divCelulas(dp, src):
    norm=[]
    linha=[]
    for i in range(len(dp)):
        col=[]
        for j in range(len(dp[i])):
            col.append(dp[i][j]/src[j])
        linha.append(col)
    norm.append(linha)
    return (norm)

    
def listZero(size):
    lista=[]
    for i in range(size):
        lista.append(0)
    return lista

def somacoluna(dp):    
    tmp=dp[:]
    soma=listZero(len(tmp[0]))
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            soma[j]+=tmp[i][j]
    return (soma)

def somalinha(pmlaux):
    soma=0
    for i in range(len(pmlaux)):
        soma+=pmlaux[i]
    return soma
    
def modulo(x):
    if(x<0):
        return x*-1
    else:
        return x
main()
