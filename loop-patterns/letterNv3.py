# *   *
# **  *
# * * *
# *  **
# *   *

#If the structure changes a bit, we should also be able to adapt to it.
n = int(input("Enter an odd integer"))

if n<3:
    print("The number must be greater than or equal to 3.\n")

else:
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n -1 or i == j: #(initial star) or (end star) or (diagonal star)
                print("*", end="")
            else:
                print(" ", end="")
        print()