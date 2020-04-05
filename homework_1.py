import math
grams = input ("Enter the weight in grams: ")
kilo = float(grams)/1000
tone = kilo/1000
print("There are", kilo, "kilos or", tone ,"tones in", grams, "grams" )
byte = input ("Enter the amount of the information in bytes: ") 
kbt = float(byte)/1000
mgbt = kbt / 1000
print("There are", kbt, "kylobytes or", mgbt ,"megabytes in", byte, "bytes" )
first = input ("Enter the first number: ")
second = input ("Enter the second number: ")
first,second = second,first
print("The first number - ",first,"the second number - ",second)
print("""Enter the width and the height of the rectangle to calculate its 
area and perimeter""")
wid = float(input("width: "))
height = float(input ("height: "))
area = wid*height
perimeter = 2 * (wid + height)
print("The area of rectangle is: ",area)
print("The perimeter of rectangle is: ",perimeter)
rad = float(input("Enter radius of a circle to calculate its area and perimeter "))
ar = 3.14 * rad*rad
perimeter = 2*3.14*rad
print("The area of the circle is: ",ar)
print("The perimetr of the circle is : ",perimeter)
print ("Enter the length of two cathets")
n = float(input("Enter the first cathet "))
m = float(input("Enter the second cathet "))
hyp = math.sqrt(n*n + m*m)
print ("The hypothenus is: ",hyp)
input()