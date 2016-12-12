def concordanciaParcial(per, p, q):
    c=[]
    for i in range(len(per)):
        linha=[]
        for j in range(len(per)):
            if per[i]<=(per[j]-p):
                linha.append(0.0)
            elif per[i]>(per[j]-q):
                linha.append(1.0)
            else:
                sub=per[i]-per[j]
                if sub <0:
                    sub*=-1
                    sub=p-sub
                else:
                    sub=p-sub
                linha.append(sub/(p-q))
        #print(linha)
        c.append(linha)
    return c

def discordanciaParcial(per, p, v):
    c=[]
    for i in range(len(per)):
        linha=[]
        for j in range(len(per)):
            if per[i]>per[j]-p:
                linha.append(0.0)
            elif per[i]<(per[j]-v):
                linha.append(1.0)
            else:
                sub=per[j]-per[i]-p
                linha.append(sub/(v-p))
        #print(linha)
        c.append(linha)
    #print("\n")
    return c
def somadeC(cp, i, j):
    soma=0.0
    for k in range(len(cp)):
        c=cp[k]
        soma+=c[i][j]*w[k]        
    return soma

def verifica(cg, i, j, dp):
    result=True
    for k in range(len(dp)):
        d=dp[k]
        if d[i][j] > cg:
            result=False    
    return result

def multiplicatori(cg, i, j, dp):
    mult=1.0
    for k in range(len(dp)):
        d=dp[k]
        if d[i][j]>cg:
            mult*=((1-d[i][j])/(1-cg))
    return mult

def ordenacao(i,j,s,c):
    if s[i][j]>=c:
        if s[j][i]>=c:
            return "I"
        else:
            return "P"
    else:
        if s[j][i]>=c:
            return "R"
        else:
            return "P-"           
    
a=["George", "John", "Mike", "Bob", "Paul"]
alt=[
    [14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 11.0, 11.0],
    [11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0,  9.0, 10.0, 10.0],
    [ 9.0,  9.0,  9.0,  9.0,  9.0,  9.0,  9.0, 10.0, 12.0, 12.0],
    [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 13.0,  9.0,  9.0],
    [ 8.0,  8.0,  8.0,  8.0,  8.0,  8.0,  8.0,  8.0,  8.0,  8.0]
    ]
per=[]
for i in range(10):
    linha=[]
    for j in range(5):
        linha.append(alt[j][i])
    print(linha)
    per.append(linha)

w=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]#peso
p=[3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]
q=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
v=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#v=[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
cg=[
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0]
    ]#concordancia global

cp=[]#concordancia parcial

for i in range(len(per)):
    #print(i+1)
    cp.append(concordanciaParcial(per[i], p[i], q[i]))
    #print("\n")
somaW=0.0
for i in range(len(w)):
    somaW+=w[i]
#print(somaW)
for i in range(len(cg)):
    for j in range(len(cg[i])):
        somaC=somadeC(cp, i, j)
        cg[i][j]=somaC/somaW
print("\n Índices de Concordancia")
for i in range(len(cg)):
    print(cg[i])
dp=[]
print("\n Índices de Credibilidade")
for i in range(len(per)):
    dp.append(discordanciaParcial(per[i], p[i],v[i]))
s=[
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0]
    ]
for i in range(len(s)):
    for j in range(len(s[i])):
        if verifica(cg[i][j], i, j, dp):
            s[i][j]=cg[i][j]
        else:
            s[i][j]=cg[i][j]*multiplicatori(cg[i][j], i, j, dp)
    print(s[i])
mo=[
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0]
    ]
c=0.75#nivel de corte
print("\n Matriz de Ordenação")
for i in range(len(s)):
    for j in range(len(s[i])):
        mo[i][j]=ordenacao(i,j,s,c)
    print(mo[i])


