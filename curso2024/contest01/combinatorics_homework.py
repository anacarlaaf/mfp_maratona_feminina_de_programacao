t = int(input())
for i in range(t):
    a, b, c, m = map(int, input().split())
    pares = 0
    for j in [a, b, c]:
        if j >= 2:
            pares += j-1
        if pares == m:
            break
        elif pares > m:

    print(pares)
    if pares == m:
        print("YES")
    else:
        print("NO")
AAAABBCCC 2
CAABACBCA

CAABACBAC
CaBACBAC
_______

