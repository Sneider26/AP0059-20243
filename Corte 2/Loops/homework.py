a = input("Enter a number: ")
a = int(a)
b = input("Enter a number: ")
b = float(b)
c = a + b

if a == b:
  print("equal")
else:
  print("different")

print("Type of a is: ", type(a))
print("Type of b is: ", type(b))
print("c = ", c)

if type(a) == type(b):
  print("a and b are of the same type")
else:
  print("a and b are of different type")
