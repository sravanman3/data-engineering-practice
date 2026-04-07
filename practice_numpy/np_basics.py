import numpy as np

arr = np.array([10,20,30,40,50])

arr = arr + 10
print(arr)

arr1 = arr + 10
print(arr1)

tax = arr * 0.1
print(tax)

total = arr + tax
print(total)

mixed_arr = np.array([10, -20, 30, -50])
mask = mixed_arr > 0
print(mask)

prices = np.array([1000,2000,3000])
discount = 0.2
final_prices = prices *(1-discount) #- (prices * discount)
print(final_prices)


amounts = np.array([100, -50, 200, 0, 300])
valid_amounts = amounts[amounts > 0]
amounts[amounts<0] = 0
print(valid_amounts)
print(amounts)


amounts = np.array([100, -20, 0, 50, -5, 80])

positive_mask = amounts >0
negative_mask = amounts <0
zero_mask = amounts ==0
print(f"positive_mask: {positive_mask}")
print(f"negative_mask: {negative_mask}")
print(f"zero_mask: {zero_mask}")