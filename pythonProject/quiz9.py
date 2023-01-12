class SoldoutError(Exception):
    pass

bread = 10
waiting = 1 # the market is full inside, waiting list starts from 1
while(True):
    try:
        print("[Leftover bread : {0}]".format(bread))
        order = int(input("How many bread do you want to order?"))
        if order > bread: # order > leftorder
            print("We don't have enough bakery.")
        elif order <= 0:
            raise ValueError
        else:
            print("[Waiting List {0}] {1} breads are ready for you."\
                  .format(waiting, order))
            waiting += 1
            bread -= order

        if bread == 0:
            raise  SoldoutError
    except ValueError:
        print("You put the wrong value.")
    except SoldoutError:
        print("Sorry, All bakeries are sold out.")
        break