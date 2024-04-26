from datetime import datetime

def check_month(month):
    if month > 12 or month < 1:
        month=datetime.now().month
    return month

def get_day_num(day):
    days = {
        'Sunday': 1,
        'Monday': 2,
        'Tuesday': 3,
        'Wednesday': 4,
        'Thursday': 5,
        'Friday': 6,
        'Saturday': 7,
    }
    return days[day]

def get_occupied_days(days_in_month, dates, month): 
    occupied_days = []
    for num in days_in_month:
        for date in dates:
            if num >= date.booking_start.day and num <= date.booking_end.day:
                if date.booking_end.month == month or date.booking_start.month == month:
                    occupied_days.append(num)
    return occupied_days

def get_cal(days_in_month, colored_days, first_day):
    count = 1
    days_in_month.reverse()
    array_2d = [[0 for _ in range(7)] for _ in range(5)]
    for i in range(5):
        for j in range(7):
            if count >= first_day and days_in_month:
                aday = days_in_month.pop()
                if aday in colored_days:
                    array_2d[i][j] = [aday, 1]
                else:
                    array_2d[i][j] = [aday, 0]
            else:
                count+=1
                array_2d[i][j] = [0,0]

    return array_2d

def get_link_args(month, year):
    arg_dic = {
        'next_year': year,
        'next_month': month + 1,
        'prev_year': year,
        'prev_month': month - 1
    }
    if month > 11:
        arg_dic['next_year'] = year + 1 
        arg_dic['next_month'] = 1
    elif month < 2:
        arg_dic['prev_year'] = year - 1 
        arg_dic['prev_month'] = 12
    return arg_dic