# -*- coding: UTF-8 -*-# -*- coding: UTF-8 -*-
import datetime

week_day_dict = {
    0: u'星期一',
    1: u'星期二',
    2: u'星期三',
    3: u'星期四',
    4: u'星期五',
    5: u'星期六',
    6: u'星期日',
}

year_dict = u"零一二三四五六七八九"

def showtime():
    i = datetime.datetime.now()
    yearnum = str(i.year)
    year = ""
    for x in range(0, len(yearnum)):
        year = year + year_dict[int(yearnum[x])]
    month = str(i.month)
    date = str(i.day)
    hour = str(i.hour)
    minute = str(i.minute)
    second = str(i.second)
    day = week_day_dict[i.weekday()]

    ret = u"现在时刻是:" +month+u"月"+date+u"日"+hour+u"点"+minute+u"分,"+day
    return ret
