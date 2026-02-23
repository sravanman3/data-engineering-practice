#
def clean_records(records):
    valid_records = 0
    error_records = 0
    valid_records_list = []

    for item in records:
        i = item.split(",",1)
        try:
            if int(i[1]):
                valid_records += 1
                valid_records_list.append(i)
        except ValueError:
            error_records += 1
    print(f" valid records list: {valid_records_list}")
    print(f" valid records : {valid_records}")
    print(f" error records : {error_records}")

clean_records(["A,100", "B,200", "C,ERROR", "D,400","E,INVALID", "F,300"])

##########################################################################
def validate_failure(success_count, failure_count, threshold_percent):
    total_count = success_count + failure_count
    threshold = (threshold_percent * total_count) /100
    if failure_count > threshold:
        return "REJECT"
    else:
        return "PROMOTE"

print(validate_failure(40,10,20))

###########################################################################
status_list=["SUCCESS", "FAILED", "SUCCESS", "SUCCESS", "FAILED", "ERROR"]
ret_dict = {}

for status in status_list:
    if status not in ret_dict:
        ret_dict[status] = 1
    else:
        ret_dict[status] += 1
print(ret_dict)

#############################################################################
log_list = [
 "id=1 status=SUCCESS",
 "id=2 status=FAILED",
 "id=3 status=SUCCESS",
 "id=4 status=FAILED"
]
success_count = 0
failure_count = 0
failure_ids = []
for log in log_list:
    i = log.split(" ",1)
    j = i[1].split("=",1)
    if j[1] == "SUCCESS":
        success_count += 1
    elif j[1] == "FAILED":
        failure_count += 1
        failure_ids.append(i[0].split("=",1)[1])
print(success_count)
print(failure_count)
print(failure_ids)

##########################################################################

def retry_function(rec):
    if int(rec[0]) % 2 == 0:
        return "SUCCESS"
    else:
        return "FAILED"

def process_records(records):
    success_count = 0
    for record in records:
        if record[1] == "FAILED":
            new_status = retry_function(record)
            if new_status == "SUCCESS":
                success_count += 1
        else:
            success_count += 1
    return success_count

input_records = [
 ("1", "SUCCESS"),
 ("2", "FAILED"),
 ("3", "FAILED"),
 ("4", "SUCCESS")
]
print("Total success records count: " + str(process_records(input_records)))

###############################################################################
# ## Alternating binary
bin_in = "101101"
for i in bin_in:
    print(i)