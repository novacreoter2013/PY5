actual_cost = float(input("Enter the actual cost of the item: "))
sale_price = float(input("Enter the sale price of the item:"))

if (sale_price > actual_cost) :
    amount = sale_price - actual_cost
    print("THE PROFIT IS : {0}".format(amount))

else :
    print("NO PROFIT!!!!")
    loss = actual_cost - sale_price
    print("THE LOSS IS : {0}".format(loss))
    
