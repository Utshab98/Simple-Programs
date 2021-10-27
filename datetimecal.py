import datetime
from datetime import datetime

currentDateTime = datetime.today().now()
print(("\n\tDateTime calcualtor\n"))
print("current DateTime is:" +str(currentDateTime))
print()
yy = int(input("Enter Year:"))
mm = int(input("Enter month:"))
dd = int(input("Enter Day:"))
h = int(input("Enter Hour:"))
m = int(input("Enter Minutes:"))
s = int(input("Enter Seconds:"))
date = datetime(year=yy,month=mm,hour=h,minute=m,second=s)
calcualatedTimeperiod = currentDateTime-date
print("\n"+str(calcualatedTimeperiod))