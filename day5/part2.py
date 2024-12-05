testing = False

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()
ordering = []
updates = []

for line in lines:
    if "|" in line:
        ordering.append([int(line[:line.index("|")]), int(line[line.index("|")+1:len(line)])])
    elif "," in line:
        updates.append(line.split(","))
valid_updates = []
for update in updates:
    valid = True
    for num in update:
        relevant_ordering = [item for item in ordering if item[0] == int(num)]
        for order in relevant_ordering:
            second_page = str(order[1])
            if second_page not in update:
                continue
            if update.index(second_page) > update.index(num):
                continue
            else:
                valid = False
                break

    if valid:
        valid_updates.append(update)


wrong_updates = [val for val in updates if val not in valid_updates]

new_updates = []
for update in wrong_updates:
    temp_update = update
    for num in temp_update:
        relevant_ordering = [item for item in ordering if item[0] == int(num)]
        for order in relevant_ordering:
            second_page = str(order[1])
            if second_page not in temp_update:
                continue
            if temp_update.index(second_page) < temp_update.index(num):
                a, b = temp_update.index(num), temp_update.index(second_page)
                temp_update.remove(num)
                temp_update.insert(b, num)

    new_updates.append(temp_update)


total = 0
for update in new_updates:
    middle_index = int((len(update) - 1)/2)
    middle_element = int(update[middle_index])
    total = total + middle_element

print(f"total: {total}")
