from employee import Employee

employee1 = Employee("Arya", "IT", 10000)
employee2 =Employee("Kid", "Business", 20000)

employee1.display_info()
employee1.give_raise(10)
employee1.change_dept("HR")

employee2.display_info()
employee2.give_raise(5)
employee2.change_dept("Finance")
try:
    employee2.change_dept("Finance","ABC") #this should throw error
except:
    print("Error while changing department")

