class House:
    # Initialization
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # Information
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
            ,self.price, self.completion_year)

houses = []
house1 = House("Jakarta", "Apartment", "Sell", "10 billion", "2010")
house2 = House("Seoul", "Office", "Yearly paid", "5 billion", "2007")
house3 = House("New York", "Villa", "Monthly paid", "1500/150", "2000")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("There are {0} houses".format(len(houses)))
for house in houses:
    house.show_detail()