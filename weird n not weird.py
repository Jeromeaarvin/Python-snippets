def number(n):
    if n % 2 != 0:
        return "weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        return "not weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        return "weird"
    elif n % 2 == 0 and n > 20:
        return "not weird"

n = int(input("Enter a num: "))
print(number(n))
