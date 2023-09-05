mb = int(input())
n = int(input())
mb2 = mb

for i in range(n):
    d = int(input())
    mb2 += mb - d
print(mb2)