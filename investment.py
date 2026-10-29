shares = 10
share_price = 150

investment_cost = shares * share_price

print("Number of shares:", shares)
print("Original share price: $", share_price)
print("Initial investment cost: $", investment_cost)

new_share_price = 175
current_value = shares * new_share_price
profit_loss = current_value - investment_cost
percentage_return = (profit_loss / investment_cost) * 100

print("New share price: $", new_share_price)
print("Current investment value: $", current_value)
print("Profit or loss: $", profit_loss)
print("Percentage return:", percentage_return, "%")


