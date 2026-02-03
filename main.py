# 1-masala
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(7))
# 2-masala
def even_sum(a, b):
    jami = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            jami += i
    return jami

print(even_sum(3, 12))
# 3-masala
def ortachasi(lst):
    return (min(lst) + max(lst)) / 2

print(ortachasi([13, 3, 7, 21, 5, 16]))
# 4-masala
def palindrom(text):
    return text == text[::-1]

print(palindrom("aziza"))
# 5-masala
def digit_sum(n):
    jami = 0
    for digit in str(n):
        jami += int(digit)
    return jami

print(digit_sum(777))
