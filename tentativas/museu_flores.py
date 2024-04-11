qtd_flor, qtd_visitante = map(int, input().split())

# lista de quais posicoes cada visitante visitou
intervalo_visita = []
for i in range(qtd_visitante):
    l, r = map(int, input().split())
    visita = [i for i in range(l, r+1)]
    intervalo_visita.append(visita)
# print(intervalo_visita)

# contar quantas vezes cada flor foi visitada
qtd_visita_cada_flor = []
for posicao in range(1, qtd_flor+1):
    qtd_visitas = 0
    for intervalo in intervalo_visita:
        if posicao in intervalo:
            qtd_visitas += 1
    qtd_visita_cada_flor.append(qtd_visitas)
# print(qtd_visita_cada_flor)

# verificar para quais posicoes a qtd de visita é a mesma que a qtd de visitantes
posicoes = []
for i in qtd_visita_cada_flor:
    if i == qtd_visitante:
        posicoes.append(1)
    else:
        posicoes.append(0)

print(*posicoes, sep="")
