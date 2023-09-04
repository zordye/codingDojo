import random

# list1 = [44,6,4,7,43,7,8,34]
# list2 = [1,109,77]
# list3 = []



# # return the minimum of all the numbers

# def find_min(_list):
#     if len(_list) > 0:
#         min = _list[0]
#         for value in _list:
#             if value < min:
#                 min = value
#         return min

# # print(find_min(list1))
# # print(find_min(list2))
# # print(find_min(list3))


# # # return the max of all the numbers
# # def find_max(_list):
# #     if len(_list) > 0:
# #         max = _list[0]
# #         for value in _list:
# #             if value > max:
# #                 max = value
# #         return max

# # # return the average of all the numbers
# # def find_mean(_list):
# #     if len(_list) > 0:
# #         sum = 0
# #         for x in _list:
# #             sum = sum + x
# #         mean = sum / len(_list)
# #         return mean

# # print(find_mean(list1))
# # print(find_mean(list2))

# def find_median(_list):
#     if len(_list) > 0:
#         temp = []
#         median = 0
#         y = len(_list)
#         for x in range(0, y):
#             temp.append(find_min(_list))
#             _list.remove(find_min(_list))
#         if y % 2 == 0:
#             median = (temp[int(y/2)] + temp[int(y/2 - 1)])/2
#         elif y % 2 != 0:
#             median  = temp[int((y + 1)/2)]
#         return median

# print(find_median(list1))
# print(find_median(list2))
# print(find_median(list3))

# def rps(player_choice):
#     randNum = random.randint(0,2)
#     comRps = ["rock", "paper", "scissors"]
#     comChoice = comRps[randNum]
#     match player_choice:
#         case "rock":
#             if comChoice == "rock":
#                 return "draw"
#             elif comChoice == "scissors":
#                 return "win"
#             elif comChoice == "paper":
#                 return "lose"
#         case "scissors":
#             if comChoice == "rock":
#                 return "lose"
#             elif comChoice == "scissors":
#                 return "draw"
#             elif comChoice == "paper":
#                 return "win"
#         case "paper":
#             if comChoice == "rock":
#                 return "win"
#             elif comChoice == "scissors":
#                 return "lose"
#             elif comChoice == "paper":
#                 return "draw"

# print(rps("scissors"))
# print(rps("rock"))
# print(rps("paper"))


# Generate Coin Change
# Change is inevitable (especially when breaking a twenty).
# Make generateCoinChange(cents). Accept a number of American cents,
# compute and print how to represent that amount with the smallest number of coins.
# Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).
# Example output, given (87):
# quarters: 3
# dimes: 1
# nickels: 0
# pennies: 2

# coins = {"quarters" : 25, "dimes" : 10, "nickles" : 5, "pennies" : 1}

# def coin_change(amount):
#     quarters = 0
#     dimes = 0
#     nickles = 0
#     pennies = 0
#     while amount >= coins["quarters"]:
#         quarters += 1
#         amount -= coins["quarters"]
#     while amount >= coins["dimes"]:
#         dimes += 1
#         amount -= coins["dimes"]
#     while amount >= coins["nickles"]:
#         nickles += 1
#         amount -= coins["nickles"]
#     while amount >= coins["pennies"]:
#         pennies += 1
#         amount -= coins["pennies"]
#     return (f'quarters = {quarters} \ndimes = {dimes} \nnickles = {nickles} \npennies = {pennies}')

# print(coin_change(87))
# print(coin_change(1001))

# Threes and Fives
# Write a function ThreesFives() that add each value from
# 100 to 1001 (inclusive) if that value is evenly divisible
# by 3 or 5 but not both. Return the final sum.

def three_five():
    sum = 0
    for i in range(100, 1001, 1):
        if i % 3 == 0 and i % 5 != 0:
            sum += i
        elif i % 5 == 0 and i % 3 != 0:
            sum += i
    return sum

print("Sum:", three_five())