'''
Print all odd numbers from 1 to 99, inclusive, with each number on a separate
line.

Bonus Question: Can you solve the problem by iterating over just the odd
numbers?
'''

for n in range(1, 100):
    if (n % 2 == 1):
        print(n)

for n in range(1, 100, 2):
    print(n)
