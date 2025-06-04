import math

# def is_triangle_number(number: int) -> bool:
#     n = 0
#     list = []
#     total = 0
#     if number == 0:
#         return True
#     else:
#         while total < number:
#             list.append(n)
#             total = int(sum(list))
#             n=n+1
#         if total == number:
#             return True
#         else:
#             return False
                        
def is_triangle_number(number: int) -> bool:   
    if number < 0:
        return False
    discriminant = 1 + 8*number
    root = math.isqrt(discriminant)
    if root * root != discriminant:
        return False
    k = (-1 + root) / 2
    return k.is_integer()