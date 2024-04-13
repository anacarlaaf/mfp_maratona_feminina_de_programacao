soma = int(input())

modalidades = 0

if soma - 8 > 0:
    soma -= 8
    modalidades += 1
    if soma - 4 > 0:
        soma -= 4
        modalidades += 1
        if soma - 2 > 0:
            soma -= 2
            modalidades += 1
            if soma - 1 == 0:
                modalidades += 1
        else:
            modalidades += 1
    else:
        if soma - 2 > 0:
            soma -= 2
            modalidades += 1
            if soma - 1 == 0:
                modalidades += 1
        else:
            modalidades += 1
else:
    if soma == 8:
        modalidades += 1
    elif soma - 4 > 0:
        soma -= 4
        modalidades += 1
        if soma - 2 > 0:
            soma -= 2
            modalidades += 1
            if soma - 1 == 0:
                modalidades += 1
        else:
            modalidades += 1
    else:
        if soma == 2:
            modalidades += 1
        elif soma - 2 > 0:
            soma -= 2
            modalidades += 1
            if soma - 1 == 0:
                modalidades += 1
        else:
            if soma != 0:
                modalidades += 1

print(modalidades)
