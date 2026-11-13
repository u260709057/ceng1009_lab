# def is_odd(n):
#     return n % 2 == 1
#
# print(is_odd(12))

# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# print(is_leapyear(2026))

# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#         print(i, total)
# print_triangular_numbers(5)

# def is_prime (n):
#     if n < 2:
#          return False
#     for i in range (2,n):
#          if n % i == 0:
#              return False
#     return True
# print(is_prime(2))


# def reverse(s):


#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
#
# print(reverse("Hello World"))
#
# def reverse_slice(s):
#     return s[::-1]
# print(reverse_slice("Hello World"))

# def remove_all_occurrences(subs, s):
#     return s.replace(subs, " ")
# print(remove_all_occurrences("ll", "hello worlld"))

# def substitute(message, key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüwvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result += key[index]
#     return result
#
# key = "qtgzücvbnmöçasdfhjklşiğery9uıo"
# print(substitute("Hello World", key))


def remove_dubs(s):
    result = ""
    for c in s:
        if c.lower() not in result.lower():
            result += c
    return result

print(remove_dubs(input("Enter a string: ")))