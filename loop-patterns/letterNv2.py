# **    *
# * *   *
# *  *  * 
# *   * *
# *    **

n = int(input("N=?:"))

#We have another method too!
#Check the diagonal and match i == j.
for i in range(n):
    print("*", end="")  

    for j in range(n):
        if i == j:
            print("-", end="")
        else:
            print(" ", end="")

    print("*")