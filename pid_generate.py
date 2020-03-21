from datetime import date
from datetime import datetime

def get_new_pid():
    '''Generate pid in string format and t_date'''
    today = date.today()
    f = open('pid_counter', 'r')
    contents = f.read()
    f.close()
    read_date, counter = contents.split('\n')
    r_date = datetime.strptime(read_date, '%Y-%m-%d').date()

    #check if today is greater then reset
    if today > r_date:
        reset_date_counter(today)
        counter = 1
        use_date = str(today)
    else:
        use_date = str(r_date)
        counter = int(counter)

    yy = use_date[2:4]
    mm = use_date[5:7]
    dd = use_date[-2:]
    if counter < 10:
        pid = yy + dd + mm + '0' + str(counter)
    else:
        pid = yy + dd + mm + str(counter)

    #return pid, use_date
    print(pid, use_date)

def reset_date_counter(t_date):
    f = open('pid_counter', 'w+')
    f.write(str(t_date))
    f.write('\n')
    f.write('1')
    f.close()

def increment_counter(use_date, counter):
    counter += 1
    counter = str(counter)
    f = open('pid_counter', 'w+')
    f.write(use_date)
    f.write('\n')
    f.write(counter)
    f.close()

get_new_pid()