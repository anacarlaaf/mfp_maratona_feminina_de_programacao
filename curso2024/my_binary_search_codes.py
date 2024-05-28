def binary_search(item, inicio, final, ar):
    if inicio > final:
        return -1
    else:
        meio = (inicio+final)//2
        if ar[meio] == item:
            return meio
        elif ar[meio] > item:
            return binary_search(item, inicio, meio-1)
        else:
            return binary_search(item, meio+1, final)


def binary_search2(item, arr, tam):
    inicio, final = 0, tam-1
    while inicio <= final:
        meio = (inicio+final)//2
        if arr[meio] == item:
            return meio
        elif arr[meio] > item:
            final = meio-1
        else:
            inicio = meio+1
    return -1