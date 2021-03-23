# Try the exercises below

# Print the date in format year-month-day
import time

timenow = time.localtime(time.time())
year,month,day,hour,minute = timenow[0:5]

print(str(year) + "/" + str(month) + "/" + str(day))
