
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
    print(f"Update: {update}")
    for num in update:
        print(f"working on number {num}")
        relevant_ordering = [item for item in ordering if item[0] == int(num)]
        print(f"Relevant ordering rules to consider: {relevant_ordering}")
        for order in relevant_ordering:
            second_page = str(order[1])
            if second_page not in update:
                print(f"no rules about {second_page}, continue")
                continue
            if update.index(second_page) > update.index(num):
                print(f"{num} comes before {second_page}, continue")
                continue
            else:
                print(f"Update {update} is invalid, skipping")
                valid = False
                break

    if valid:
        valid_updates.append(update)
print()
print()
print(valid_updates)
total = 0

for update in valid_updates:
    middle_index = int((len(update) - 1)/2)
    middle_element = int(update[middle_index])
    total = total + middle_element

print()
print()
print(total)