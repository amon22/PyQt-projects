def date():
    import datetime
    data = {}
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November",
              "December"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    date = datetime.datetime.now()
    weekday = date.weekday()

    data["month"] = months[date.month]
    data["day"] = str(date.day)
    data["weekday"] = days[weekday]

    return data

if __name__ == "__main__":
   print date()["month"]+" "+ date()["day"] + "," + date()["weekday"]