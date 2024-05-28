def minimum_towers(n, cubes):
    towers = []

    for cube in cubes:
        placed = False

        for tower in towers:
            if cube <= tower[-1]:
                tower.append(cube)
                placed = True
                break

        if not placed:
            towers.append([cube])

    return len(towers)


n = int(input())
cubes = list(map(int, input().split()))

print(minimum_towers(n, cubes))
