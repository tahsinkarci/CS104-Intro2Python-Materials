# *   *      
# *  *      
# * *
# *  *
# *   *

k = int(input("K=?:"))

for i in range(k):
    if i < k // 2:
        print("*", end="")
        print(" " * (k//2 + 1 - i), end="")
        print("*")
    else:
        print("*", end="")
        print(" " * (i - k//2 + 1), end="")
        print("*")
        