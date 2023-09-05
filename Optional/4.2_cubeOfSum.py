max_num = int(input())

for i in range(max_num + 1):
    string_sum = 0

    for char in str(i):
        string_sum += int(char)

    if (string_sum ** 3) == i:
        print(i)