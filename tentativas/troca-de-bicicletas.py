T = int(input())

for i in range(T):  # n de casos de testes

    N = int(input())  # n de amigos
    lista = input()
    lista_int = [int(i) for i in lista.split()]  # separar lista e transformar em int

    for j in range(N):
        lista_int = [lista_int[-1]] + lista_int[:-1]
        print(lista_int)
