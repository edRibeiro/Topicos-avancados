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

    dp=[
        [##1 - preço
            [1,4,9],
            [(1/4),1,4],
            [(1/9),(1/4),1]
        
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


    fp=[
        [1.0, 8.0, 2.0, 3.0, 1.0, 4.0, 9.0],
        [1/8, 1.0, 7.0, 7.0, 1/9, 3.0, 4.0],
        [1/2, 1/7, 1.0, 2.0, 1.0, 6.0, 8.0],
        [1/3, 1/7, 1/2, 1.0, 1/2, 6.0, 7.0],
        [1.0, 9.0, 1.0, 2.0, 1.0, 9.0, 9.0],
        [1/4, 1/3, 1/6, 1/6, 1/9, 1.0, 1.0],
        [1/9, 1/4, 1/8, 1/7, 1/9, 1.0, 1.0]
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
            
    norm = normalizar(alt, crt, dp)
    print ("\nDesempenho das alternativas à luz dos critérios normalizados")
    for i in range(len(norm)):
        for j in range(len(norm[i])):
            print("\n",crt[i]," ",alt)
            for k in range(len(norm[i][j])):
                print (alt[k]," ",norm[i][j][k])

    ##PRIORIDADES MÉDIAS LOCAIS
    print("\nPML's à luz dos criterios.\n")
    pml=[]
    for i in range(len(norm)):
        pml.append(calcularPML(norm[i]))
        print("\n",crt[i],"=",pml[i])
    print("\nPML's à luz do Foco Principal.\n")
    pmlfp=calcularPMLFP(fp)
    for i in range(len(pmlfp)):
        print("\n",crt[i],"=",pmlfp[i])
    ##PRIORIDADES MÉDIAS GLOBAIS

    pg=[]
    
####################################################################
##def calcularPG(
def calcularPMLFP(dp):
    pml=[]
    for i in range(len(dp)):
        somalinha=0
        for j in range(len(dp[i])):
            somalinha+=dp[i][j]
        somalinha/=len(dp[i])
        pml.append(somalinha)
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
        
def normalizar(alt, crt, dp):
    scrt=[]
    norm=[]
    for i in range(len(dp)):
        scrt.append(somacoluna(dp[i]))
    for i in range(len(dp)):
        norm.append(divCelulas(dp[i], scrt[i]))
    return norm
##    print ("\nDesempenho das alternativas à luz dos critérios normalizados")
##    for i in range(len(norm)):
##        for j in range(len(norm[i])):
##            print("\n",crt[i]," ",alt)
##            for k in range(len(norm[i][j])):
##                print (alt[k]," ",norm[i][j][k])
                
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
    ##print(soma)
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            soma[j]+=tmp[i][j]
    return (soma)

def somaLinha():
    return
main()
