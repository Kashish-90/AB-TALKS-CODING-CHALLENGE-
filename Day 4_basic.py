a=int(input("ENTER THE FIRST NUMBER:"))
operator=input("ENTER THE OPERATOR(+,-,*,/):")
b=int(input("ENTER THE SECOND NUMBER:"))
if "+" :
print(a+b)
elif operator== "-" :
print(a-b)
elif operator== "*":
print(a*b)
elif operator== "/":
if (b==0):
print("ERROR OCCURED:DIVISION BY ZERO NOT POSSIBLE")
else:
print(a/b)
else:
print("INVALID OPERATION")
