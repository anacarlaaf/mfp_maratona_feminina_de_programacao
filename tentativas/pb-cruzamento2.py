n_plantas = int(input())
plantas = input()

plantas = [int(p) for p in plantas.split(" ")]
planta = plantas[0]
del plantas[0]

pares = []

for i in plantas:
    pares.append([planta, i])
