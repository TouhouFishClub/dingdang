# -*- coding: UTF-8 -*-# -*- coding: UTF-8 -*-
import datetime

week_day_dict = {
    0: '星期一',
    1: '星期二',
    2: '星期三',
    3: '星期四',
    4: '星期五',
    5: '星期六',
    6: '星期天',
}

def showtime():

    i = datetime.datetime.now()


    year = str(i.year)
    month = str(i.month)
    date = str(i.day)
    hour = str(i.hour)
    minute = str(i.minute)
    second = str(i.second)
    day = week_day_dict[i.weekday()]

    ret = "现在时间是:" +year+"年"+month+"月"+date+"日"+hour+"点"+minute+"分,"+day
    return ret
