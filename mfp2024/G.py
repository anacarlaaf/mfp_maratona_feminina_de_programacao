n = int(input())

notas = []
for i in range(n):
    notas.append(input())
formatado = []
for i in notas:
    formatado.append(i[5:].split())
formatado2 = []
for i in formatado:
    ponto = int(i[1][1])
    formatado2.append([int(i[0]), ponto])

pontos1 = 0
pontos2 = 0
for i in formatado2:
    if i[0] == 1:
        pontos1 += i[1]
    else:
        pontos2 += i[1]
print(pontos1, "x", pontos2)
