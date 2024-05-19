import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    if a < b:
        if b < c:
            print("STAIR")
        elif b > c:
            print("PEAK")
        else:
            print("NONE")
    else:
        print("NONE")
