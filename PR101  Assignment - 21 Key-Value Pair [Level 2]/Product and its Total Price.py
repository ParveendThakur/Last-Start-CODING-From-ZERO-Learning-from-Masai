def solve(products, prices, quantities):
    
# Create a dictionary to store product name and total price pairs
    product_prices = {}

# Calculate total price for each product and store in the dictionary
    for i in range(n):
        total_price = prices[i] * quantities[i]
        product_prices[products[i]] = total_price

# Output
    for product, price in product_prices.items():
        print(product, '{:.2f}'.format(price))

