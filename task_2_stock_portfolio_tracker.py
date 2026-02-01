print("Welcome to the Stock portfolio tracker: ")

stock_prices={
    "AAPL":180,
    "TSLA":250,
    "GOOG":140
}

total_value=0
print("Available stocks:",stock_prices)

n=int(input("How many different stocks do you have? "))

for i in range(n):
    stock_name=input("Enter stock name: ").upper()
    quantity=int(input("Enter quantity: "))

    if stock_name in stock_prices:
        total_value=total_value+(stock_prices[stock_name]*quantity)
    else:
        print("Stock not found!")

print("Total investement value is: ",total_value)