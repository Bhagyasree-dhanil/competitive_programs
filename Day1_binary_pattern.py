"""
Generate all binary strings
if n=1  [0,1]
if n=2  [00, 01, 10, 11]
if n=3  [000, 001, 010, 011, 100, 101, 110, 111]

"""


def append_bits(s1, b_arr):
    return [s1 + i for i in b_arr]


def generate_bits(n):
    if n == 0:
        return []
    if n == 1:
        return ['0', '1']
    else:
        return append_bits('0',generate_bits(n-1)) + append_bits('1', generate_bits(n - 1))


# test case
n = [0, 1, 2, 5]

for i in n:
    print(generate_bits(i))