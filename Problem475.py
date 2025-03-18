#import sys

MOD = int(1e9 + 7)
n = 600
N = n // 3 + 10

# Initialize DP and combinatorial tables
f = [[[0] * N for _ in range(N)] for _ in range(N)]
cb = [[0] * N for _ in range(N)]
fac = [1] * N

f[n // 3][0][0] = 1

# Compute binomial coefficients
for i in range(N):
    for j in range(i + 1):
        cb[i][j] = (cb[i - 1][j - 1] + cb[i - 1][j]) % MOD if j else 1

# Compute factorials
for i in range(1, N):
    fac[i] = fac[i - 1] * i % MOD

# Dynamic programming loop
for i in range(n // 3, -1, -1):
    for j in range(n // 3, -1, -1):
        for k in range(n // 3, -1, -1):
            if f[i][j][k]:
                for a in range(min(4, i) + 1):
                    for b in range(min(4 - a, j) + 1):
                        c = 4 - a - b
                        if c > k:
                            continue
                        x = (
                            cb[j][b] * cb[k][c] % MOD * fac[b] % MOD * fac[c] % MOD *
                            cb[4][a] % MOD * cb[4 - a][b] % MOD
                        )
                        f[i - a][j - b + a][k - c + b] = (
                            f[i - a][j - b + a][k - c + b] + f[i][j][k] * x % MOD
                        ) % MOD

ans = f[0][0][0]
print(ans)
