import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    D, A, B, F = map(int, input().split())
    i = D/(A+B)
    print(f'#{tc+1}', F*i)