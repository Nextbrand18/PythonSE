import datetime
now = datetime.datetime.now()
#print(now)
#print(now.day)
#print(datetime.datetime.today().weekday())
weekdaydict = {0: "Sunday",
               1: "Monday",
               2: "Tuesday",
               3: "Wednesday",
               4: "Thursday",
               5: "Friday",
               6: "Saturday"}
print(weekdaydict[datetime.datetime.today().weekday()])
