# Link dos problemas: https://codeforces.com/group/WYIydkiPyE/contest/450037/attachments/download/20669/MFP.pdf
# Problem I. Complicações logísticas

a = int(input())

# estamos quase lá, só precisamos revisar algumas coisas da lógica

moradores = []
distancias = []
for i in range(a):
    soma_distancias = 0
    museu = 0
    c, distancia = input().split()
    distancia = int(distancia)
    if c == "+":
        moradores.append(distancia)
    else:
        moradores.remove(distancia)
    if moradores:
        diferenca = max(moradores) - min(moradores)
        if diferenca % 2 != 0:
            museu = (diferenca+1)/2
        else:
            if diferenca == 2:
                museu = 2
            else:
                museu = (diferenca/2)+1
        for j in moradores:
            if j > museu:
                soma_distancias += j-museu
            elif j < museu:
                soma_distancias += museu-j
        distancias.append(int(soma_distancias))
    else:
        distancias.append(-1)
for i in distancias:
    print(i)
