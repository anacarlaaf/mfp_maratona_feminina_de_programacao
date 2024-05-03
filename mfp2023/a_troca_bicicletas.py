# Link dos problemas: https://codeforces.com/group/WYIydkiPyE/contest/450037/attachments/download/20669/MFP.pdf
# Problem A. Troca de Bicicletas

# import sys
# sys.stdin = open("input.txt", "r")

testes = int(input())

for i in range(testes):
    amigos = int(input())
    original = [int(a) for a in input().split()]
    for j in range(1, len(original)+1):
        percurso = [j]  # toda bike começa com seu dono
        n = j
        salvar = original.index(j)+1
        while True:
            if n == salvar:  # confere se a bike está com seu dono a cada troca
                break
            else:
                percurso.append(original[n-1])  # se não, salva o pi amigo que receberá a bike
                n = original[n-1]  # o novo n é o n amigo que recebeu a bike
        print(*percurso)
