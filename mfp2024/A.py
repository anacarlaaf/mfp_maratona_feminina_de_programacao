n, p = map(int, input().split())
forcas = list(map(int, input().split()))

tempo = max(forcas)*p
forcas.remove(max(forcas))
forcas = sorted(forcas, reverse=True)
for i in forcas:
    tempo -= i*p

print(tempo)
