
with open("matrix.txt", "r") as file:
    outer_list = []
    sum_of_num = 0
    count_of_negative = 0
    max_num = None
    for line in file:
        inner_list = []
        for val in line.split():
            try:
                num = int(val.strip())
                if num%2 == 0:
                    inner_list.append("*")
                else:
                    inner_list.append("#")
                sum_of_num += num
                if num < 0:
                    count_of_negative += 1
                if max_num is None or max_num < num:
                    max_num = num
            except ValueError:
                continue
        outer_list.append(inner_list)
    # for line in outer_list:
    #     for i in range(len(line)):
    #         if max_num < line[i]:
    #             max_num = line[i]

    print(outer_list)
    print(sum_of_num)
    print(count_of_negative)
    print(max_num)
