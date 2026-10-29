# **    *
# * *   *
# *  *  * 
# *   * *
# *    **

n = int(input("N=?:"))

#Now, we can do the same for N.

for i in range(n):    
    print("*", end="")#We should always put * at the beginning.
    print(" " * (i), end="")#We should decide the number of spaces for the first gap: initially 0, then incremented by 1, like y = x.
    print("*", end="")#Put another *
    print(" " * (n - i - 1), end="")#Now, decrease from some number 1 by 1: y = b - x, where b is n-1.
    print("*")