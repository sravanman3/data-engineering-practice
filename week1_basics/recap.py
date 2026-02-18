records = [
    {"name": "Alice", "dept": "IT"},
    {"name": "Bob", "dept": "HR"},
    {"name": "Charlie", "dept": "IT"},
    {"name": "David", "dept": "Finance"},
]

reverse_dict = {}
for record in records:
    if record["dept"] not in reverse_dict:
        reverse_dict[record["dept"]] = [record["name"]]
    else:
        reverse_dict[record["dept"]].append(record["name"])

print(reverse_dict)