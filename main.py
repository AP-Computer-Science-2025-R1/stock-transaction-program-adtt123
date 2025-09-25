shares = 1000
initial_share = 32.87
commission = 0.02
final_share = 33.92
stock_cost_int = shares * initial_share
stock_cost_fin = shares * final_share

print("Joe paid $", stock_cost_int, "for the stock.")
print("Joe paid his broker $", stock_cost_int * commission, "when he bought the stock.")
print("Joe sold the stock for $", stock_cost_fin)
print("Joe paid his broker $", stock_cost_fin * commission, "when he sold the stock.")

total_money = stock_cost_fin - stock_cost_int
money_left = total_money - ((stock_cost_fin * commission) + (stock_cost_int * commission))
rounded_money_left = round(money_left, 2)
if money_left > 0:
    print("Joe made a profit of $", rounded_money_left)
else:
    print("Joe made a loss of $", rounded_money_left)