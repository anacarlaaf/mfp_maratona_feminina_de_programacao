n = int(input())
cubes = list(map(int, input().split()))
# USAR BISECT


def b_search(item, torres, inicio, fim):
    meio = (inicio + fim) // 2
    opcao = fim
    if inicio == fim:
        return meio
    else:
        while inicio < fim:
            meio = (inicio + fim) // 2
            if torres[meio] == item:
                return meio
            elif torres[meio] > item:
                opcao = meio
                fim = meio-1
            else:
                inicio = meio + 1
    return opcao


towers = [cubes[0]]
qtd = 1
maior = cubes[0]
maior_idx = 0
menor = cubes[0]

for i in range(1, n):
    if cubes[i] <= menor:
        menor = cubes[i]
        towers[0] = cubes[i]
    elif cubes[i] >= maior:
        maior = cubes[i]
        towers.append(cubes[i])
        maior_idx += 1
        qtd += 1
    else:
        base = b_search(cubes[i], towers, 1, qtd-1)
        if base == maior_idx:
            maior = cubes[i]
        towers[base] = cubes[i]

print(len(towers))
