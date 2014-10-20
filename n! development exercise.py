#Ryan Cox
#16/10/14 (fixed on 19/20/10)
#Development exercis - factorial program

n = int(input("input value of n: "))


if n>=0:
    f = 1
    while (n > 0):
        f = f * n
        n = n - 1


print(f)
