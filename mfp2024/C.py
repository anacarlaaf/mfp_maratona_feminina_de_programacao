n = int(input())
postos = list(map(int, input().split()))

moedas = 0
k = 1
while k < 2**(n-1):
    moedas += postos[k-1]
    if 2*k+1 <= len(postos):


print(moedas)
