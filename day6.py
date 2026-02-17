# employee_file = open("employees1.txt","a")
#
# # print(employee_file.read())
#
# employee_file.write("\nEric - MD")
#
# employee_file.close()
#
#
#
# with open("employee1.txt","r+") as file:
#     # print(file.read())
#     file.write("\nEric - MD")
#     print(file.read())


#######################################
#######################################
# # Challenge 1
###import datetime
# from datetime import datetime
# time_now = datetime.now().strftime("%Y-%M-%D %H-%M-%S")
#
# def log_message(message):
#     with open("app.log","a") as log_file:
#         log_file.write(f"{time_now} - {message} \n")
#
#
# log_message("User logged in")
# log_message("File Uploaded")

# # Challenge 2
# employees = [
#     "Alice - IT",
#     "Bob - HR",
#     "Charlie - IT"
# ]
#
# # works but not efficient
# # for employee in employees:
# #     with open("clean_employees.txt","a") as f:
# #         f.write(employee+"\n")
#
# ## cleaner version
# with open("clean_employees.txt","w") as emp_file:
#     for employee in employees:
#         emp_file.write(employee + "\n")
#
# # # Challenge 3
with open("nums.txt","r") as f, open("negatives.txt","w") as n_file, open("positives.txt","w") as p_file:
    for line in f:
        num = int(line.strip())
        if num >= 0:
            p_file.write(line)
        else:
            n_file.write(line)
