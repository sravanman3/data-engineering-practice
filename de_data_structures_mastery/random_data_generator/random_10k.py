def generate_random_sales(no_of_transactions):

    import random

    sales = []
    cust_list = ["Alice","Bob","Charlie","David","Eve","Frank"]
    product_list = ["Electronics","Grocery","fashion","books"]

    for i in range(no_of_transactions):
        txn_id = f"T{i+1}"
        customer = random.choice(cust_list)
        product = random.choice(product_list)

        amount = random.choices(
            [random.randint(10,100),
             -random.randint(10,100),
             "Invalid"
             ],
            weights=[80,10,10]
        )[0]

        # sales.append((txn_id,customer,product,amount))

        yield txn_id, customer, product, amount
    # return sales