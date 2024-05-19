# Link do problema: https://vjudge.net/contest/627742#problem/F

n, x = map(int, input().split())
ar = list(map(int, input().split()))

indices = {}
repetidos = {}
for i in range(n):
    if ar[i] in indices:
        repetidos[ar[i]] = i
    else:
        indices[ar[i]] = i

print(indices)
print(repetidos)
par = []
sim = False
for i in range(n):
    if x-ar[i] in indices:
        if indices[ar[i]] == indices[x-ar[i]]:
            if indices[x-ar[i]] in repetidos:
                par = [indices[ar[i]]+1, repetidos[x-ar[i]]+1]
                sim = True
                break
            else:
                sim = False
        else:
            par = [indices[ar[i]]+1, indices[x-ar[i]]+1]
            sim = True
            break
    else:
        sim = False
if sim:
    print(*par)
else:
    print("IMPOSSIBLE")
