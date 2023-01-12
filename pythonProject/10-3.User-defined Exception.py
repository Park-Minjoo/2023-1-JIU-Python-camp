class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("Division Calculation for a Single Digit")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("input : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("[Value Error] Wrong Number, please put the single digit")
except BigNumberError as err:
    print("[Big Number Error] Something goes wrong, please put the single digit")
    print(err)
finally:
    print("Thank you for using this calculator.")


