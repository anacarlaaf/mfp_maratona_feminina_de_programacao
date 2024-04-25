# Link dos problemas: https://codeforces.com/group/WYIydkiPyE/contest/450037/attachments/download/20669/MFP.pdf
# Problem C. Zigue-Zague

distancia, metros = input().split()
distancia = int(distancia)
metros = int(metros)

# raiz de 2 sobre 2 (sen(45°)
sen45 = (2**(1/2))/2
tamanho_corda = distancia/sen45

percurso = 0

# qtd de vezes que ela atravessou de um lado pro outro
atravessou = metros//tamanho_corda
faltando = metros-(atravessou*tamanho_corda)

# cada vez que atravessa, o x aumenta a distância entre os prédios (pois os catetos são iguais, já que o ângulo é 45)
x = atravessou * distancia + faltando * sen45
if atravessou % 2:
    y = distancia - faltando * sen45
else:
    y = faltando * sen45

print(round(x, 10), round(y, 10))
