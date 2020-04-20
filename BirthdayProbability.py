# There is a 50% probability that at least 2 persons will share the same birthday
# if you picked 23 persons randomly
from datetime import datetime
import random

print(datetime.now())
count = 0
for _ in range(100000):
    bday_list = ([random.randrange(366) for i in range(23)])
    if len(bday_list) != len(set(bday_list)):
        count += 1
print(count)
print(datetime.now())

# print(datetime.datetime.now())
# count = 0
# for _ in range(1000000):
#     bday_list = ([random.randrange(366) for i in range(23)])
#     seen = set()
#     for bday in bday_list:
#         if bday in seen:
#             count += 1
#             break
#         else:
#             seen.add(bday)
# print(count)
# print(datetime.datetime.now())
