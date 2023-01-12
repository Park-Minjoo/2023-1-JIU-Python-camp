# Normal Price
def price(people):
    print("The price of {0} people is {1}.".format(people, people * 10000))

# Discount Price for children
def price_child(people):
    print("The price of {0} child is {1}".format(people, people * 5000))

# Discount Price for baby
def price_baby(people):
    print("The price of {0} babies is {1}".format(people, people * 1000))