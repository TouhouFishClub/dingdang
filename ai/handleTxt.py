#-*-encoding:utf-8 -*-
import weather
import timeai


def handletxt(txt):
    txt = txt.strip()
    try:
        txt = txt.decode("utf-8")
    except:
        pass
    if txt.find(u"天气")>1 and len(txt)<8 :
        ret = weather.getWeather(txt)
    elif txt.find(u"行情")>0:
        ret = ""
    elif txt.find(u"几点") >= 0 or txt.find(u"报时") >= 0:
        ret = timeai.showtime()
    else:
        ret = ""
    return ret
