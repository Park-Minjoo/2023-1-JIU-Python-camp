def std_weight(height, gender):
    if gender == 'male':
        return height * height * 22
    else:
        return height * height * 21

height = 153.7 # cm
gender = 'female'
weight = round(std_weight(height / 100, gender),2) # m
print("The normal weight of {0}cm, {1} is {2}kg".format(height, gender, weight))