alt=[
    [14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 11.0, 11.0],
    [11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0,  9.0, 10.0, 10.0],
    [ 9.0,  9.0,  9.0,  9.0,  9.0,  9.0,  9.0, 10.0, 12.0, 12.0],
    [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 13.0,  9.0,  9.0],
    [ 8.0,  8.0,  8.0,  8.0,  8.0,  8.0,  8.0,  8.0,  8.0,  8.0]
    ]
peso=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
soma=0
for i in range(len(peso)):
    soma+=peso[i]
for i in range(len(peso)):
    peso[i]/=soma
#w=0.1
c=[
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0]
   ]
for i in range(len(c)):
    for j in range(len(c[i])):
        for k in range(len(alt[i])):
            if(alt[i][k]>=alt[j][k]):
                c[i][j]+=peso[k]#w
print("\nConcordancia I")
for i in range(len(c)):
    print(round(c[i][0],1), round(c[i][1],1), round(c[i][2],1), round(c[i][3],1), round(c[i][4],1))

escalas=[]

for lin in range(len(alt[0])):
    cri=[]
    for col in range(len(alt)):
        cri.append(alt[col][lin])
    minValor=min(cri)
    maxValor=max(cri)
    dif=maxValor-minValor
    escalas.append(dif)
maxdif=max(escalas)
d=[
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0]
   ]
for i in range(len(d)):
    for j in range(len(d[i])):
        for k in range(len(alt[i])):
            r=(alt[j][k]-alt[i][k])/maxdif
            if r<0:
                d[i][j]=0.0
            else:
                d[i][j]=r
             
print("\nDiscordancia I")
for i in range(len(d)):
    print(round(d[i][0],1), round(d[i][1],1), round(d[i][2],1), round(d[i][3],1), round(d[i][4],1))

veto=[]


C=1.0
D=0.0

for i in range(len(c)):
    linha=[]
    for j in range(len(c[i])):
        #print(c[i][j]," >= ",C,d[i][j],"<=", D, "?")
        if c[i][j]==C and d[i][j]<=D:
            linha.append(1)
        else:
            linha.append(0)
    veto.append(linha)
        
print("\nMatriz Veto preenchida")
for i in range(len(veto)):
    print(" %.1f" % veto[i][0], " %.1f" % veto[i][1],
          " %.1f" % veto[i][2], " %.1f" % veto[i][3], " %.1f" % veto[i][4])           


