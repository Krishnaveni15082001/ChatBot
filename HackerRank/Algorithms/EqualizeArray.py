from collections import Counter

def solve(a):
    c = Counter(a)
    
    print(len(a) - max(c.values()))


pepe = int(input())
arr = [int(x) for x in input().split()]

solve(arr)

