# *   *      
# *  *      
# * *
# *  *
# *   *


k = int(input("K=?:"))
#If the question asks, you can implement an if-else here to check the input consistency.

#We can decide how the gap changes according to the increase in the rows.

#Think of it like F(x): as x increases, the number of gaps should decrease until the middle.
#Like a function y = b - m * x, where m is positive.

#After the middle, it should increase.
#Like a function y = m * x + b.
for i in range(k):
    if i < k // 2: #until the middle
        print("*", end="")
        print(" " * (k - 2 - i), end="") #If the question asks for a nested loop, change this line to a loop.
        print("*")
    else: #after the middle
        print("*", end="")
        print(" " * (i-1), end="")
        print("*")

#However, for larger K values, the middle joint starts to separate. Why?
#Because we did not fix the number of gaps to 1 in the middle.
#It should be fixed to 1 at the middle point k//2.
#We should start from (k//2 + 1) and decrease 1 by 1, k//2 times, until the middle.
#Please check the version 2 code.
#Run both with different K values.
        