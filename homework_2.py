n = int(input ("Enter an integer number "))
if n%4 == 0 :
    m = " is even number and divides into 4 without remainer"
elif n%2 == 0 :
    m = "  even number, but doesn't devides into 4"
else: m = " is odd number"
print(n, m)

n = int(input ("Enter an integer number "))
if n%2 != 0 :
    m = "is odd number"
else : m =  "is even number"
if n%5 == 0 :
     m += " and divides into 5 without remainer"
else : m += " and doesn't divide into 5 without remainer"
print(n, m)

n = float(input ("Enter a number "))
if n > 0 :
     m =  "is a positive number"
elif n < 0 :
    m =  "is a negative number"
else :  m = "is zero"
print(n, m)

n = int(input ("Enter the number of your seat "))
if n%2 == 0:
    m = "Oh,you have an upper seat"
else : m = "Congratulations! You have a lower berth"
if n <= 36 :
        m += " in an compartment"
else :
        m += " from the side"
print (m)
input()
