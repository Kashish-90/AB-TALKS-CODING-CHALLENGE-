numbers=[4,8,7,9,10,16,5,8]
#Sum
total=0
for num in numbers:
  total+=num
print("Sum=",total) 
#Max
maximum=numbers[0]
for num in numbers:
  if num>maximum:
    maximum=num

print("Max=",maximum)
#Min
minimum=numbers[0]
for num in numbers:
  if num<minimum:
    minimum=num
print("Min=",minimum)
#frequency count
frequency={ }
for num in numbers:
  if num in frequency:
    frequency[num]+=1
  else:
    frequency[num]=1
print("Frequency=",frequency)
#Reverse list
reversed_list=[ ]
for i in range(len(numbers)-1,-1,-1):
  reversed_list.append(numbers[i])
print("Reversed List=",reversed_list)
