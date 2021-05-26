for _ in range(int(input())):
    m = int(input())
    if m > 37:
        if m % 5 >= 3:
            m += 5 - m % 5
    print(m)

