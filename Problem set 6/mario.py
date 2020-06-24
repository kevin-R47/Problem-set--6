while True:
    n = cs50.get_int("Height: ")
    if n > 0 and n < 9:
        break
for i in range(1, n + 1):
    if n == 0:
        continue
    print(" "*(n-i),end="")
    print("#"*i)
