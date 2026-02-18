import datetime as datetime
import logger as logger
import load as load_data

def extract_it_emp():
    err_counter = 0
    it_emp_counter = 0
    with open("employees.txt","r") as emp_file:
        start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.log_msg(f"Started at {start_time}")
        it_employees = []

        for emp in emp_file:
            emp = emp.strip()
            if "-" in emp:
                name, dept = emp.split("-",1)
                name = name.strip()
                dept = dept.strip()
                if dept and dept != "":
                    if dept.upper() == "IT":
                        it_employees.append(name + ": " + dept)
                        it_emp_counter += 1
                else:
                    logger.log_msg(f"Invalid dept for emp: {name}")
                    err_counter += 1
            else:
                logger.log_msg(f"invalid data for emp: {emp}")
                err_counter += 1
        load_data.load_data(it_employees)
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.log_msg(f"Total no of invalid records: {err_counter}")
        logger.log_msg(f"Total no of IT employees: {it_emp_counter}")
        logger.log_msg(f"Ended at {end_time}")

extract_it_emp()