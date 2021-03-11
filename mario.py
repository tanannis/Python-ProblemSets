from cs50 import get_int  # cs50 library from Harvard University

while True:
    height = get_int("height: ")

    if height < 1 or height > 8:
        height = get_int("height: ")
    if height > 0 and height < 9:
        break

for i in range(height):
    # print spaces
    print(" " * (height - 1 - i), end="")
    # print hashes
    print("#" * (i + 1))
