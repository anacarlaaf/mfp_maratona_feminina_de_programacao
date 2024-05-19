t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    problems = [a for a in range(1, n+1)]
    rev_problems = problems.copy()
    rev_problems.reverse()

    if k == n-1:
        print(*problems)
    elif k == 0:
        print(*rev_problems)
    else:
        primeiros = k+1
        order = problems[-primeiros:] + rev_problems[primeiros:]
        print(*order)
