# Link do problema: https://vjudge.net/contest/627742#problem/D

n = int(input())
lista = list(map(int, input().split()))
lista.sort()

faltando = 0
completa = [i for i in range(1, n+1)]

ultimo = False
for j in range(n-1):
    if lista[j] != completa[j]:
        print(completa[j])
        ultimo = False
        break
    else:
        ultimo = True
if ultimo:
    print(completa[-1])

