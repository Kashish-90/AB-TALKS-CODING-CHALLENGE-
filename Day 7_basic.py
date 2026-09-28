prices=[7,1,2,6,9,4]  #array
min_price=price[0]    #minimum price
max_profit=0
buy_day=0
sell_day=0
temp_buy_day=0
for i in range(1,len(prices)):
  if prices[i]<min_price:
    min_price=price[1]
    temp_buy_day=i
profit=prices[i]-min_price
if profit>max_profit:
  max_profit=profit
  buy_day=temp_buy_day
  sel_day=i
print("Maximum Profit=",max_profit)
print("Buy on Day",buy_day+1)
print ("Sell on Day",sel_day+1)
