def load_data(emp_data):
    with open("it_employees.txt", "w") as it_emp_file:
        for emp in emp_data:
            it_emp_file.write(emp + "\n")