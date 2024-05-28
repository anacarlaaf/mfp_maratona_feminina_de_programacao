# Problema: https://vjudge.net/contest/629594#problem/D

def binary_search(item, arr, tam):
    inicio, final = 0, tam-1
    while inicio <= final:
        meio = (inicio+final)//2
        if arr[meio] == item:
            return meio
        elif arr[meio] > item:
            final = meio-1
        else:
            inicio = meio+1
    return -1


n, q = map(int, input().split())
ar = list(map(int, input().split()))

for i in range(q):
    buscar = int(input())
    print(binary_search(buscar, ar, n))
