# Link dos problemas: https://codeforces.com/group/WYIydkiPyE/contest/450037/attachments/download/20669/MFP.pdf
# Problem D. Constante Mística do Universo

m1, m2 = map(float, input().split())

# sempre diferentes
x1, x2 = map(float, input().split())

f = float(input())

distancia = abs(x1-x2)

G = f*distancia**2/(m1*m2)

print(round(G, 10))
