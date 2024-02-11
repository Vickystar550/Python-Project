import  datetime as dt

today = dt.datetime.now()
print(today)

formatted_date = today.strftime("%Y-%m-%d")

print(formatted_date)
