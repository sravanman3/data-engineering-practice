def log_msg(log_message):
    with open("log_file.txt", "a") as log_file:
        log_file.write(str(log_message) + "\n")