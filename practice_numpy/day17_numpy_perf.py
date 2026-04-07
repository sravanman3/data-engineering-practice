import numpy as np
import time
arr = np.random.randint(-100,1000,size=1_000_000)
print(len(arr))

start_time = time.time()
tax_list= []
for x in arr:
    tax_list.append(x*0.1)
end_time = time.time()

print("loop time: ", end_time-start_time)

start = time.time()
tax = arr * 0.1
end = time.time()
print("np time: ", end-start)

start = time.time()
result = []
for x in arr:
    if x > 0:
        tax = x*0.1
        total= x+ tax
        result.append(total)
end = time.time()
print("loop ETL time: ",end-start)
print(len(result))

start = time.time()
valid = arr[arr>0]
tax = valid * 0.1
total = valid + tax
end = time.time()
print("numpy ETL time:", end-start)
print(len(valid))