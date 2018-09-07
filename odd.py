from datetime import datetime
import time
import random

# odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
#         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#         41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

odds = range(1, 60, 2)
print(list(odds))
print(odds.count(3))
for i in range(5):
    right_this_minutes = datetime.today().second
    print(right_this_minutes)
    if right_this_minutes in odds:
        print("this minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1, 6)
    print(wait_time)
    time.sleep(wait_time)
