#Convert string to datetime

#daeutil

from dateutil import parser

date_time = parser.parser("Oct 14 1997 7:50AM")
print(date_time)



# #datetime module
# from datetime import datetime

# date="Oct 14 1997 7:50AM"

# date_time=datetime.strptime(date,"%b %d %Y %I:%M%p")
# print(date_time)