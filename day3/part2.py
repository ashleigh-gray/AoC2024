import re

testing = False

if testing:
    filename = "sample_input2.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()
all_multis = []

def multi(item):
    numbers = re.findall("\\d{1,3}", item)
    return int(numbers[0]) * int(numbers[1])

total_lines = ''
for line in lines:
    total_lines += line

total_lines = re.sub("don't\\(\\).*?do\\(\\)", '', total_lines)
total_lines = re.sub("don't\\(\\).*?$", '', total_lines)
valid = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", total_lines)
for item in valid:
    numbers = re.findall("\\d{1,3}", item)
    multi = int(numbers[0]) * int(numbers[1])
    all_multis.append(multi)

print(sum(all_multis))