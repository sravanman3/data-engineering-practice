from sales_pipeline.extract import extract

def test_extract():
    extract_result = extract.extract_sales("test_sales.csv")

    total_records = extract_result["total_records"]
    extract_errors = extract_result["extract_errors"]

    assert total_records == 5
    assert extract_errors == 3

test_extract()

def test_extract_empty():
    extract_result = extract.extract_sales("empty_sales.csv")

    assert extract_result["errors"] == ['Empty file received']

test_extract_empty()


