import weather

def handletxt(txt):
    if txt.endswith(u"天气") and len(txt)<8 :
        ret = weather.getWeather(txt)
    elif txt.index(u"行情")>0:
        ret = ""
    else:
        ret = ""
    return ret