import re

testing = False

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()

first_list = []
second_list = []
distance = []

for line in lines:
    digits = re.findall(r'[^ ]+',line)
    first_digit = int(digits[0])
    second_digit = int(digits[1])
    first_list.append(first_digit)
    second_list.append(second_digit)

sorted_first_list = sorted(first_list)
sorted_second_list = sorted(second_list)

for i in range(len(sorted_first_list)):
    dist = abs(sorted_first_list[i] - sorted_second_list[i])
    distance.append(dist)

print(sum(distance))
