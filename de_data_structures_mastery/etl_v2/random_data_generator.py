import random

def random_generator(no_of_txns):
    customer_list = ["Alice","Bob","Charlie","David","Eve","Frank"]
    product_list = ["Electronics","Grocery","books","Clothing","Furniture"]
    for i in range(no_of_txns):
        txn_id = f"T{i+1}"
        customer = random.choice(customer_list)
        product = random.choice(product_list)
        amount = random.choices(
            [random.randint(1,500),
             -random.randint(1,100),
             "INVALID"],
           weights=[80,10,10]
        )[0]

        yield txn_id,customer,product,amount

