list1 = [44,6,4,7,43,7,8,34]
list2 = [1,109,77]
list3 = []



# return the minimum of all the numbers

def find_min(_list):
    if len(_list) > 0:
        min = _list[0]
        for value in _list:
            if value < min:
                min = value
        return min

# print(find_min(list1))
# print(find_min(list2))
# print(find_min(list3))


# # return the max of all the numbers
# def find_max(_list):
#     if len(_list) > 0:
#         max = _list[0]
#         for value in _list:
#             if value > max:
#                 max = value
#         return max

# # return the average of all the numbers
# def find_mean(_list):
#     if len(_list) > 0:
#         sum = 0
#         for x in _list:
#             sum = sum + x
#         mean = sum / len(_list)
#         return mean

# print(find_mean(list1))
# print(find_mean(list2))

def find_median(_list):
    if len(_list) > 0:
        temp = []
        median = 0
        y = len(_list)
        for x in range(0, y):
            temp.append(find_min(_list))
            _list.remove(find_min(_list))
        if y % 2 == 0:
            median = (temp[int(y/2)] + temp[int(y/2 - 1)])/2
        elif y % 2 != 0:
            median  = temp[int((y + 1)/2)]
        return median

print(find_median(list1))
print(find_median(list2))
print(find_median(list3))
