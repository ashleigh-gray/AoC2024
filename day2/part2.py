import numpy as np
import itertools
testing = False

def powerset(s):
    return list(itertools.combinations(s, len(s)-1))

def check_safety(reports):
    diffs = np.diff(reports)
    safe_decreasing = np.all(-4 < diffs) & np.all(diffs < 0)
    safe_increasing = np.all(4 > diffs) & np.all(diffs > 0)
    safe = safe_decreasing or safe_increasing
    return safe

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()
safe_count = 0

for line in lines:
    reports = [int(x) for x in line.split(" ")]
    safe = check_safety(reports)
    if safe:
        safe_count += 1
    else:
        subsets = [x for x in powerset(reports)]
        for subset in subsets:
            subset = list(subset)
            safe = check_safety(subset)
            if safe:
                safe_count += 1
                break

print(safe_count)

