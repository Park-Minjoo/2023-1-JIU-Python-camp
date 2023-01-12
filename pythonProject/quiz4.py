# (Output Example)
# -- The winner of a lottery --
# Chicken : 1
# Coffee : [2,3,4]
# -- Congratulations --
#
# (Usage Example)
# from random import *
#
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)  # shuffle the output in the list
# print(lst)
# print(sample(lst, 1))  # randomly pick one value from the list

from random import *
users = range(1, 21) # generate num from 1 to 20
# print(type(users))
users = list(users)
# print(type(users)) # change type to list
print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print("-- The winner of a lottery --")
print("Chicken : {0}".format(winners[0]))
print("Coffee : {0}".format(winners[1:]))
print("-- Congratulations --")