T = int(input())
for i in range(T):
    S = input().strip()
    if S == S[::-1]:
        print(1)
    else:
        print(0)
