class Aggregator:
    def __init__(self):
        self.rev_per_customer = {}
        self.rev_per_product = {}
        self.total_amount = 0
        self.total_count = 0
        self.product_count = {}


    def process(self,txn):
        txn_id,customer,product,amount = txn

        #revenue per customer
        self.rev_per_customer[customer] = self.rev_per_customer.get(customer,0) + amount

        self.rev_per_product[product] = self.rev_per_product.get(product,0) + amount

        #totals
        self.total_amount += amount
        self.total_count += 1

        #product_count
        self.product_count[product] = self.product_count.get(product,0) + 1
