import math
def make_readable(seconds):
    if seconds<60:
        if seconds < 10:
            return f'00:00:0{seconds}'
        else:
            return f'00:00:{seconds}'
    if seconds>=60 and seconds < 3600:
        minute = math.floor(seconds/60)
        second = seconds - minute*60
        if second < 10:
            second_str = f':0{second}'
        else:
            second_str = f':{second}'
        if minute < 10:
            minute_str = f':0{minute}'
        else:
            minute_str = f':{minute}'
        return f'00{minute_str}{second_str}'
    if seconds>=3600:
        hour = math.floor(seconds/3600)
        seconds = seconds - hour*3600
        minute = math.floor(seconds/60)
        second = seconds - minute*60
        if hour < 10:
            hour_str = f'0{hour}'
        else:
            hour_str = f'{hour}'
        if second < 10:
            second_str = f':0{second}'
        else:
            second_str = f':{second}'
        if minute < 10:
            minute_str = f':0{minute}'
        else:
            minute_str = f':{minute}'
        return f'{hour_str}{minute_str}{second_str}'