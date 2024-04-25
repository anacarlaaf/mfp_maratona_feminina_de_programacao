# Link dos problemas: https://codeforces.com/group/WYIydkiPyE/contest/450037/attachments/download/20669/MFP.pdf
# Problem E. Código

digitos = input().split()
digitos = [int(i) for i in digitos]

uns = 0
dig_seguranca = digitos[-1]
del digitos[-1]

for i in digitos:
    if i == 1:
        uns += 1

if uns % 2 != 0 and dig_seguranca == 0:
    print("S")
elif uns % 2 == 0 and dig_seguranca == 1:
    print("S")
else:
    print("N?")
