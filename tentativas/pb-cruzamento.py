# ler a quantidade de plantas
n_especimes = int(input())

# ler as alturas de cada planta
n_alturas = input()
plantas = [int(i) for i in n_alturas.split(" ")]

# salvar em uma lista todas as configurações de pares possíveis
pares_possiveis = []

lista_alturas = plantas

pares = []
alturas_usadas = []
for n, i in enumerate(lista_alturas):
    for m, j in enumerate(lista_alturas):
        if n != m and m not in alturas_usadas and n not in alturas_usadas:
            if [i, j] not in pares and [j, i] not in pares:
                pares.append([i, j])
                alturas_usadas.append(n)
                alturas_usadas.append(m)
    pares_possiveis.append(pares)

for i in pares_possiveis:
    print(i)
