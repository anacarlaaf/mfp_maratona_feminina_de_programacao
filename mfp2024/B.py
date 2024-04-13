c1x, c1y = map(int, input().split())
c2x, c2y = map(int, input().split())
c3x, c3y = map(int, input().split())
c4x, c4y = map(int, input().split())

coord = [[c1x, c1y], [c2x, c2y], [c3x, c3y], [c4x, c4y]]

base = 0
altura = 0

coord_base = []
for n, i in enumerate(coord):
    for m, j in enumerate(coord):
        if n!=m and i[1] == j[1]:
            coord_base.append(i)
            coord_base.append(j)
        break

coord_altura = []
for n, i in enumerate(coord):
    for m, j in enumerate(coord):
        if n!=m and i[0] == j[0]:
            coord_altura.append(i)
            coord_altura.append(j)
        break

base = coord_base[0][0] - coord_base[1][0]
base = abs(base)

altura = coord_altura[0][1] - coord_altura[1][1]
altura = abs(altura)

area = base*altura
print(area)