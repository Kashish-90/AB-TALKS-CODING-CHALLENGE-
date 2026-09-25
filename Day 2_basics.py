marks=float(input("enter marks:"))
if marks<0 or marks>100:
  print("Invalid Marks")
elif marks>=90:
  print ("Grade: A")
  print("Status:Passed")
elif marks>=75:
  print ("Grade:B")
  print("Status:Passed")
elif marks>=50:
  print ("Grade:C")
  print("Status:passed")
else:
  print("Grade:FAIL")
  print("Status:Failed")
  
  
