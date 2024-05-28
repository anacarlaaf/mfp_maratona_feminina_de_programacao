import sys
sys.stdin = open("input.txt", "r")

n, q = map(int, input().split())
ar = list(map(int, input().split()))

soma1 = 0
somas = {}
for i in range(n):
    soma1 += ar[i]
    somas[i+1] = soma1
for i in range(q):
    a, b = map(int, input().split())
    print(somas[b]-somas[a]+ar[a-1])
