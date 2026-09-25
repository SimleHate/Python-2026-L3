#Ex1
import math

radius = float(input("Enter circle radius? "))
area = math.pi * radius ** 2
print(f"Circle area = {area}")


#Ex2
temp_in_Celcius = float(input("Enter the temperature in Celsius? "))
Fahrenheit = temp_in_Celcius * 1.8 + 32
print(f"Fahrenheit = {Fahrenheit}")


#Ex3
n = int(input("Enter a number? "))
if (n <= 1): 
    print( n, "is not prime")
else:
    prime = True
    for i in range (2, n):
        if n%i==0:
            prime = False
            break
    if prime:
        print(n, "is prime")
    else:    
        print (n, "is not prime")


#Ex4
def perfect_num(n):
  if n <= 1:
    print(f"{n} is NOT perfect number!")
    return False
  m = 0
  for i in range(1, n):
    if n % i == 0:
      m =+ i

  return m == n

n = int(input("Enter a number?"))
if perfect_num(n):
  print(f"{n} is perfect number!")
else:
  print(f"{n} is NOT perfect number!")


#Ex5
av = ["red", "blue", "yellow", "green"]
color = input("Your color? ")
if color in fav:
    print("yo same!")
    print (f"position at {fav.index(color)}")
else:
    print("nonono")


#Ex6
range1 = list(range(0,7))
range2 = list(range(1,11,3))
range3 = list(range(5,0,-1))
range4 = list(range(6,-3,-2))

print("All range", range1, range2, range3, range4)


#Ex7
s = input ("Enter String:")
s1 = s.replace("$", "")
print(s1)


# Ex8
def extract_even(l):
    result = []
    for x in l:
        if x % 2 == 0:
            result.append(x)
    return result


print(extract_even([1, 4, 5, -1, 10]))


#Ex9
def factorial_calculation(n):
    if n < 0:
        return False

    result = 1
    for i in range(1, n + 1):
        if i == 0:
          result = 1
        result *= i
    return result

print(factorial_calculation(0))


#Ex10
def divs(n):
    out = []
    for i in range (1, n+1):
        if n % i == 0:
            out += [i]
    return out
    
print (divs(120))



#Ex11
import math
xa = int(input("xa "))
xb = int(input("xb ")) 
ya = int(input("ya "))
yb = int(input("yb "))
dist = math.sqrt((xa - ya)**2 + (xb-yb)**2)
print (dist)


#Ex12
col = int(input("cols: "))
row = int(input("rows: "))
for i in range (row):
    for j in range (col):
        if i == 0 or i== row - 1 or j ==0 or j == col - 1:
            print ("* ", end="")
        else:
            print ("  ", end="")
    print()        
    


