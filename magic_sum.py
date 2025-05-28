# Basic solution
def magic_sum(arr):
    odds = []
    for num in arr:
        if num % 2 == 1 and '3' in str(num):
            odds.append(num)
    return sum(odds)


# Better solution using list comprehension
def magic_sum(arr):
    return sum(i for i in arr if i % 2 and '3' in str(i))