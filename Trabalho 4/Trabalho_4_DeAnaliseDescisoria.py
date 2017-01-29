import math 
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


    fp=[
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
            
    norm = normalizar(dp)
    print ("\nDesempenho das alternativas à luz dos critérios normalizados")
    for i in range(len(norm)):
        for j in range(len(norm[i])):
            print("\n",crt[i]," ",alt)
            for k in range(len(norm[i][j])):
                print (alt[k]," ",norm[i][j][k])
                
    normFP = normalizarFP(fp)
    print(normFP)
    print ("\nDesempenho dos criterios à luz do Foco peincipal normalizado")
    print("\nFoco Principal ",crt)
    for k in range(len(normFP)):
        print (crt[k]," ",normFP[k])
    

    ##PRIORIDADES MÉDIAS LOCAIS
    print("\nPML's à luz dos criterios.\n")
    pml=[]
    for i in range(len(norm)):
        pml.append(calcularPML(norm[i]))
        print("\n",crt[i],"=",pml[i])
    print("\nPML's à luz do Foco Principal.\n")
    pmlfp=calcularPMLFP(normFP)
    for i in range(len(pmlfp)):
        print("\n",crt[i],"=",pmlfp[i])
    ##PRIORIDADES MÉDIAS GLOBAIS

    pg=calcularPG(pml,pmlfp)

    ##Iniciar analise de inconsistencia
    
####################################################################

def inconsistencia(dp, pml):
    n=len(dp)
    ic=(autovalores(dp, pml)-n)/(n-1)##autovalores deve ser uma matriz
    
def autovalores(dp, pml):
    dp2=[]
    for h in range(len(dp)):
        linha=[]
        for i in range(len(dp[h])):
            col=[]
            for j in range(len(dp[h][i])):
                col.append(dp[h][i][j]*pml[h][j])
            linha.append()
        dp2.append(linha)
    pri=[]
    for i in range(len(dp)):
        pri.append(somacoluna(dp2[i]))
    pml2=[]
    for i in range(len(pri)):
        col=[]
        for j in range(len(pri[i])):
            col.append(pri[i][j]/dp2[i][j][j])
        pml2.append(col)
    ##criar somalinha para somar as linhas de pml2 e dividir pela ordem da matriz e armasenar o resultado de cada linha em um vetor
    
    
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
        print("A",(i+1),":",round(pg[i],2))
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
def somalinha():##criar implementaçoã
def modulo(x):
    if(x<0):
        return x*-1
    else:
        return x
main()
