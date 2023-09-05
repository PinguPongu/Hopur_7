import math

number_of_waves = int(input())
number_of_lines = int(input())
radians_per_line = number_of_waves * 2 * math.pi / number_of_lines

for i in range(number_of_lines):
    r = i * radians_per_line

    for j in range(int(math.sin(r) * 20) + 20):
        print("X", end="")
    print()