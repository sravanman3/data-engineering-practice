class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary


    def display_info(self):
        print(self.name)
        print(self.dept)
        print(self.salary)

    def give_raise(self, increment):
        if increment >= 0:
            self.salary = self.salary + (self.salary*(increment/100))
            print(f"increased salary {self.salary}")
        else:
            print("Negative increment can not be made")

    def change_dept(self, new_dept):
        old_dept = self.dept
        self.dept = new_dept
        print(f"employee moved from {old_dept} to {self.dept}")

