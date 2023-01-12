print("Division Calculator")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the Second number : "))
print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# try:
#     print("Division Calculator")
#     num1 = int(input("Enter the first number : "))
#     num2 = int(input("Enter the Second number : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("ERROR! You enter the wrong number.")
# except ZeroDivisionError as err: # Zero Error
#     print(err)
#
# try:
#     print("Division Calculator")
#     nums = []
#     nums.append(int(input("Enter the first number : ")))
#     nums.append(int(input("Enter the Second number : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("ERROR! You enter the wrong number.")
# except ZeroDivisionError as err: # Zero Error
#     print(err)
# except:
#     print("Something goes wrong.")