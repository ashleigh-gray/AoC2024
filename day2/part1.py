import numpy as np
testing = False

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()
safe_count = 0

for line in lines:
    reports = [int(x) for x in line.split(" ")]
    diffs = np.diff(reports)
    safe_decreasing = np.all(-4 < diffs) & np.all(diffs < 0)
    safe_increasing = np.all(4 > diffs) & np.all(diffs > 0)
    safe = safe_decreasing or safe_increasing
    print(f"{reports} {diffs} {safe}")
    if safe:
        safe_count += 1

print(safe_count)

