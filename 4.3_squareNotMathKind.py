size = int(input())

for i in range(size):
    for j in range(size):
        if j == 0 or j == (size - 1) or i == 0 or i == (size - 1):
            print("*", end="")
        else:
            print(" ", end="")
 
    print("\n")