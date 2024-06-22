import sys
from datetime import datetime
from datetime import timedelta

#question 1
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print("{0}\t{1}".format(item, cost))

#question 2

print(datetime.now() - timedelta(seconds=60))

print(datetime.now() + timedelta(days=730))



#question 3
from datetime import timedelta
d = timedelta(days=100, hours=10, minutes=13)
print((d.days, d.seconds, d.microseconds))


#question 4
#get current date
datetime_object = datetime.now()
print(datetime_object)
print('Type :- ',type(datetime_object))

feet = 2
inches = 3
totinch = feet * 12 + inches
print("when converting feet to inches, the total amount of inches are", totinch)

