# Link dos problemas: https://codeforces.com/group/WYIydkiPyE/contest/450037/attachments/download/20669/MFP.pdf
# Problem I. Complicações logísticas

# Excedeu o tempo -_-) Temos que reorganizar a lógica

a = int(input())

moradores = set([])
distancias = []
for i in range(a):
    soma_distancias = 0
    museu = 0
    c, distancia = input().split()
    distancia = int(distancia)
    if c == "+":
        moradores.add(distancia)
    else:
        moradores.remove(distancia)

    if moradores:
        diferenca = max(moradores) - min(moradores)
        if len(moradores) == 1:
            distancias.append(0)
        elif diferenca == 1 or diferenca == 2:
            distancias.append(diferenca)
        else:
            if diferenca % 2 == 0:
                museu = min(moradores) + diferenca/2
            else:
                museu = min(moradores) + (diferenca-1)/2
            museu = int(museu)
            if museu not in moradores:
                for j in range(museu-1, min(moradores)-1, -1):
                    if j in moradores:
                        museu = j
                        break
                    elif (museu + museu - j) in moradores:
                        museu = museu + museu - j
                        break
            for k in moradores:
                soma_distancias += abs(museu-k)
            distancias.append(soma_distancias)
    else:
        distancias.append(-1)
for i in distancias:
    print(i)
