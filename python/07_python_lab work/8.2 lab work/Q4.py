





products = {'Laptop': 60000, 'Phone': 30000, 'Tablet': 20000, 'Watch': 15000}

highest = max(products, key=products.get)
print("Product with highest price:", highest, "=", products[highest])
