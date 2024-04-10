n = int(input())
alturas = input()
lista_alturas = [int(i) for i in alturas.split(" ")]

planta1 = lista_alturas[0]
del lista_alturas[0]

possibilidades = []
pares_possiveis = []
for i in lista_alturas:
    par = [planta1, i]
    pares_possiveis.append(par)

for i in pares_possiveis:
    possibilidades.append([i])

for i in possibilidades:
    l_alturas = lista_alturas.copy()
    a = i[0][1]
    # l_alturas.remove(a)
    usados = [l_alturas.index(a)]
    for n, j in enumerate(l_alturas):
        for m, k in enumerate(l_alturas):
            if n not in usados and m not in usados:
                if n!=m and [[j, k], [k, j]] not in i:
                    i.append([j, k])
                    usados.append(n)
                    usados.append(m)

for i in possibilidades:
    print(i)

# verificar qual tem a soma maior
# lista_filhas = []
# for i in possibilidades:
#     filhas = []
#     for j in i:
#         sum(j)/2