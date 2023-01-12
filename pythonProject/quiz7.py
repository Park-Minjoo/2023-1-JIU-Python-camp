# - Week X weekly report -
# Depart:
# Name:
# Description:

for i in range(1, 51):
    with open("Week" + str(i) + ".txt", "w", encoding='utf8') as report_file:
        report_file.write("- Week {0} weekly report -".format(i))
        report_file.write("\nDepart: ")
        report_file.write("\nName: ")
        report_file.write("\nDescription: ")