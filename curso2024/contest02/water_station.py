# Link do problema: https://vjudge.net/contest/627742#problem/C

n = int(input())
points = [i for i in range(0, 101, 5)]
position = round(n/5)
print(points[position])
