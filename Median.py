import math

sales_prices = [100, 83, 220, 40, 100, 400, 10, 1, 3]

sorted_list = sorted(sales_prices)
num_sales = len(sorted_list)
half_slice = math.floor(num_sales/2)

median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_sales)

print(median)