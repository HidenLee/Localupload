from functools import reduce
print(reduce(lambda x, y: x - y, [0, 1, 2, 3, 4]),reduce(lambda x, y: y + x, 'aaaae'))

print(list(filter(lambda x: (x+1) % 2, range(10))))
