# Link dos problemas: https://codeforces.com/group/WYIydkiPyE/contest/450037/attachments/download/20669/MFP.pdf
# Problem A. Troca de Bicicletas

testes = int(input())

for i in range(testes):
    amigos = int(input())
    permutacao = [int(a) for a in input().split()]
    for j in range(1, len(permutacao)+1):
        sequencia = []
        print(i, *sequencia)