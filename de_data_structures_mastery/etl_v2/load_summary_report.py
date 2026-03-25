
def load_summary_report(filename,total_transactions,valid_txns,error_txns,
                        rev_per_customer,rev_per_product,top_customers,avg_order_value,most_popular_product):
    with open(filename,"w") as file:
        file.write(f"ETL SUMMARY REPORT\n")
        file.write("----------------------------\n")


        file.write(f"Total Transactions: {total_transactions}\n")
        file.write(f"Valid Transactions: {valid_txns}\n")
        file.write(f"Error Transactions: {error_txns}\n\n")

        file.write(f"Avergae Revenue: {round(avg_order_value,2)}\n\n")

        file.write(f"Top 3 Customers by Revenue\n")
        file.write("----------------------------\n")
        print(top_customers)
        for cust,revenue in top_customers:
            file.write(f"{cust}: {round(revenue,2)}\n")

        file.write("Revenue Per Product\n")
        file.write("----------------------------\n")
        print(rev_per_product)
        for prod,revenue in rev_per_product.items():
            file.write(f"{prod}: {round(revenue,2)}\n")

        file.write("\nMost Popular Product\n")
        file.write(f"{most_popular_product[0] }: {most_popular_product[1]}\n")
