'''
Found the correct format for MySQL datetime field

https://dev.mysql.com/doc/refman/5.7/en/datetime.html

The DATETIME type is used for values that contain both date and time parts. 
MySQL retrieves and displays DATETIME values in 'YYYY-MM-DD HH:MM:SS' format. 
The supported range is '1000-01-01 00:00:00' to '9999-12-31 23:59:59'.

I just need to figure out how to get the python object into that string format now
'''

import datetime

time_raw = datetime.datetime.now()
time_format = datetime.datetime.strftime(time_raw, '%Y-%m-%d %H:%M:%S')
print(time_format)
