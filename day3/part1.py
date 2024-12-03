import re

testing = False

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()
all_multis = []

for line in lines:
    valid = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", line)
    for item in valid:
        numbers = re.findall("\\d{1,3}", item)
        multi = int(numbers[0]) * int(numbers[1])
        all_multis.append(multi)

print(sum(all_multis))
