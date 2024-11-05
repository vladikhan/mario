from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        break

if height < 1 or height > 8:
    print("Height must be between 1 and 8 inclusive.")

# for i in range(1, height + 1):
   #   print("#" * i)

# reversed
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)
