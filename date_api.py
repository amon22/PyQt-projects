import datetime

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
date = datetime.datetime.now()
print months[date.month - 1] +" "+ str(date.day)
print days[date.weekday()]