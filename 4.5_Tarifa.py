mb_per_month = int(input())
n = int(input())

sum_mb = mb_per_month

for i in range(n):
    sum_mb += int(input())

print((n * mb_per_month) - sum_mb)