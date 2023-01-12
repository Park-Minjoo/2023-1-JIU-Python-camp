url = "https://google.com"

my_str = url.replace("https://", "") #Rule1

my_str = my_str[:my_str.index(".")] #Rule2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"


print("The password of {0} is {1}".format(url, password))