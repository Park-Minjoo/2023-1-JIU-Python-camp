# (Output Example)
# [O] 1 customer (time: 15m)
# [ ] 2 customer (time: 50m)
# [O] 3 customer (time: 5m)
# ...
# [ ] 50th customer (time: 16m)
#
# The entire number of customer : 2 people.

from random import *
cnt = 0 # the entire number of customers
for i in range(1, 51): # 1 ~ 50 (customers)
    time = randrange(5, 51) # (5m ~ 50m time)
    if 5 <= time <= 15:
        print("[0] {0} customer (time: {1}m)".format(i, time))
        cnt += 1
    else: # matching failed
        print("[ ] {0} customer (time: {1}m)".format(i, time))

print("The entire number of customer: {0} people.".format(cnt))