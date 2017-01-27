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
            [1/4,1,4],
            [1/9,1/4,1]
        
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

    print ("\nDesempenho das alternativas à luz dos critérios")
    for i in range(len(dp)):
        print("\n",crt[i]," ",alt)
        for j in range(len(dp[i])):
            print (alt[j]," ",dp[j][j])
    normal=normalizarquadros(dp)
    print ("\nDesempenho das alternativas à luz dos critérios Nomormalizados")
    for i in range(len(normal)):
        print("\n",crt[i]," ",alt)
        for j in range(len(normal[i])):
            print (alt[j]," ",normal[j][j])

    calcularPML(dp)
## prioridades médias locais (PML)    
def calcularPML(desp):
    pml=[]
    for i in range(len(desp)):
        tpml=desp[i]

        
def normalizarquadros(df):
    soma_cri=[]
    qn=[]
    for i in range(len(df)):
        soma_cri.append(somaColuna(df[i]))
    for i in range(len(df)):
        tmp=df[i][:]
        for j in range(len(tmp)):
            for l in range(len(tmp[j])):
                tmp[j][l]=tmp[j][l]/soma_cri[i][l]
        qn.append(tmp)
    return qn

    
def somaColuna(tb):
    soma=[]
    
    for i in range(len(tb[0])):
        soma.append(0)
    for i in range(len(tb)):
        for j in range(len(tb[i])):
            soma[j]+=tb[i][j]
    return soma
    
def somalinha(linha):
    soma=0.0
    for i in range(len(linha)):
        soma+=linha[i]
    return soma
main()
