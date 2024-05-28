# Problema: https://vjudge.net/contest/629594#problem/C

n = int(input())
costs = list(map(int, input().split()))
m = int(input())

ord_costs = costs.copy()
ord_costs.sort()
ord_soma = 0
ord_sums = {}
for i in range(1, n+1):
    ord_soma += ord_costs[i-1]
    ord_sums[i] = ord_soma

soma = 0
sums = {}
for i in range(1, n+1):
    soma += costs[i-1]
    sums[i] = soma

for i in range(m):
    tipo, l, r = map(int, input().split())
    if tipo == 1:
        print(sums[r] - sums[l] + costs[l-1])
    else:
        print(ord_sums[r] - ord_sums[l] + ord_costs[l-1])
