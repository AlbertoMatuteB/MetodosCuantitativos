from collections import Counter
with open('data01.txt', 'r') as fd:
    lines = fd.read().split()
    counter = Counter(lines)
    # sorts items
    items = sorted(counter.items(), key=lambda x: float(x[0]))
    # prints desired output
    total = len(items)
    print(total)
    for k in items:
        print (k[0])