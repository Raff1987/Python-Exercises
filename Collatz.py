# Martin Rafter 5-2-18
# The collatz conjecture program
n = int(input("Integer:"))
while n!= 1 : #  if answer is not equal to 1 keep running the loop 
    if n % 2 ==0: 
        n = n/2 #  if the number is even, the  number is divided by 2
        print (n) 
    else: # if the number is not even you multiple by 3 and add 1
        n = (n * 3) + 1
        print (round (n)) # The answer will always reach 1 no matter the number it starts at 
