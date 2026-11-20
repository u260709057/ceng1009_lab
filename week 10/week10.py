# L = [76,92.3 ,"hello", True , 4 , 76]
# L.append(76)
# L.append("apple")
# L.insert(0,"hello")
# L.insert(3,"cat")
#
# C = L.count(76)
# L.remove(76)
# L.pop(L.index(True))

# def sum_of_squares(xs):
#     total = 0
#     for item in xs:
#         total += item ** 2
#     return total
# print(sum_of_squares([1, 3, 3, 7, 5, 6]))


# def sumevens(xs):
#     total = 0
#     for item in xs:
#         if item %2 == 0 :
#             total += item
#     return
# print(sumevens([1,2,3,4,5,6]))

#
#
#
# def sum_evens(number_list):
#     sum = 0
#     for num in number_list:
#         if number_list in number_list:
#             sum += num
#     return sum
#
# my_list = [1,2,3,4,5,6,7,8,9,10]
# print(sum_evens(my_list))

# def count_five_letters(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# my_list = ['apple','cat', 'lemon','python','tiger']
# print(count_five_letters(my_list))

# def isiteven(numbers):
#     sum = 0
#     for n in numbers:
#         if n % 2 == 0:
#             break
#         sum += n
#     return sum
# my_list = [1, 3, 3, 7, 5, 6]
# print(isiteven(my_list))

# def count_until_sam(xs):
#     count = 0
#     for x in xs:
#         if x == "sam":
#             return count + 1
#         count += 1
#     return count
# print(count_until_sam(["asada","john","johannes", "anna" , "sam","george"]))

# def replace(s, old, new):
#     pieces = s.split(old)
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED!")
#     else:
#         print("FAİLED!")
#
# test(replace('Mississippi','i','I'),
#      'MIssIssIppI')

def find_max_value(num_list):
    max_value = num_list[0]
    for num in num_list:
        if num > max_value:
            max_value = num
    return max_value
print(find_max_value([1,2,3,4,5,6,7,8,9,10]))
print(find_max_value([-35,-35,-60,-5]))


