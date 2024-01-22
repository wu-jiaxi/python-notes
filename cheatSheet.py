def my_function():
  print("Hello from a function")

#This is a comment
print("Hello, World!")

#Variables
x = 5
y = "John"
print(x)
print(y)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

#Global Variables
x = "awesome"


def myfunc():
  print("Python is " + x)

myfunc()

#Data types

#Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Casting
#int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
#float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
#str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

#Booleans
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#Operators
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3
  

#Loop
  thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#While 
i = 1
while i < 6:
  print(i)
  i += 1