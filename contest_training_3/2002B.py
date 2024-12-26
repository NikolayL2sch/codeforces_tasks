"""
перестановки
x = y - Bob wins

"""

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    if a == b or a == b[::-1]:
        print("Bob")
    else:
        print("Alice")