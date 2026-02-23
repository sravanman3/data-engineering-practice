def flip_count(pattern):
    flip_count_pattern0 = 0
    flip_count_pattern1 = 0
    start_bin = pattern[0]
    for i in range(len(pattern)):
        if start_bin == "1":
            if i % 2 == 0 and pattern[i] == "0":
                flip_count_pattern1 += 1
            elif i % 2 == 1 and pattern[i] == "1":
                flip_count_pattern1 += 1
        elif start_bin == "0":
            if i % 2 == 0 and pattern[i] == "1":
                flip_count_pattern0 += 1
            elif i % 2 == 1 and pattern[i] == "0":
                flip_count_pattern0 += 1

    if start_bin == "1":
        return flip_count_pattern1
    else:
        return flip_count_pattern0

print(flip_count("0011"))



