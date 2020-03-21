from datetime import datetime
'''
today = date.today()
f  = open('pid_counter', 'r')
contents = f.read()
f.close()
date, count = contents.split('\n')
print(date, count)
'''
d = datetime.strptime('2020-03-20', '%Y-%m-%d').date()
print(d)
