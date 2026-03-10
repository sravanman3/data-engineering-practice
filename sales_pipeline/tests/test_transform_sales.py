from sales_pipeline.transform import transform_sales

def test_transform_sales():
    config = {
    "allowed_products": ["Electronics","Clothing","Grocery"],
      "tax_rates": {
          "Electronics": 0.18,
          "Clothing": 0.05,
          "Grocery": 0
      }
    }

    data = [{'txn_id': 'T1', 'customer': 'Alice', 'product_type': 'electronics', 'amount': '100'},
            {'txn_id': 'T2', 'customer': 'Bob', 'product_type': 'Grocery', 'amount': 'abc'},
            {'txn_id': 'T3', 'customer': 'Joe', 'product_type': 'Electronics', 'amount': '-10'},
            {'txn_id': 'T4', 'customer': 'Max', 'product_type': 'Clothing', 'amount': '10'},
            {'txn_id':'T5','customer':'Ann','product_type':'Furniture','amount':'100'}]
    result = transform_sales.transform_sales(data,config)

    print(f"valid records: {len(result["data"])}")
    print(f"error records: {len(result["errors"])}")

    assert len(result["data"]) == 2
    assert len(result["errors"]) == 3

test_transform_sales()