input_data = []
final_data = {}
temp_data = {}
max3 = [0, 0, 0]
key = 0
max_num = 0
total_sum = 0
index = 0
with open("data.txt") as file:
    for line in file.readlines():
        input_data.append(line.strip())
for data in input_data:
    if data == "":
        key += 1
    else:
        index += 1
        if key in temp_data.keys():
            temp_data[key].append(data)
        else:
            temp_data[key] = []
            temp_data[key].append(data)
for key in temp_data:
    sum_num = 0
    for number in temp_data[key]:
        sum_num += int(number)
        temp_data[key] = sum_num
for key in temp_data:
    if max3[0] < temp_data[key]:
        max3[0] = temp_data[key]
    elif max3[1] < temp_data[key]:
        max3[1] = temp_data[key]
    elif max3[2] < temp_data[key]:
        max3[2] = temp_data[key]
print(sum(max3))
print(max(temp_data.values()))
a = list(temp_data.values())
a.sort()
print(sum(a[-4:-1]))
