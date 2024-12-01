import re

testing = False

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()

first_list_count = {}
second_list_count = {}

for line in lines:
    digits = re.findall(r'[^ ]+',line)
    first_digit = int(digits[0])
    second_digit = int(digits[1])
    if first_digit not in first_list_count.keys():
        first_list_count[first_digit] = 1
    else:
        first_list_count[first_digit] += 1
    if second_digit not in second_list_count.keys():
        second_list_count[second_digit] = 1
    else:
        second_list_count[second_digit] += 1

similarity = []
for key in first_list_count.keys():
    if key in second_list_count.keys():
        sim = first_list_count[key] * (key * second_list_count[key])
        similarity.append(sim)

print(f"total {sum(similarity)}")
