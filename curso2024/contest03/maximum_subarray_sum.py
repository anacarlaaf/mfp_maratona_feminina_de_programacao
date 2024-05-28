n = int(input())
ar = list(map(int, input().split()))

max_soma = -(10**10)
aux_soma = -(10**10)
for i in ar:
    if i > aux_soma+i:
        aux_soma = i
    else:
        aux_soma += i
    if aux_soma > max_soma:
        max_soma = aux_soma
print(max_soma)
