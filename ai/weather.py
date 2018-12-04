#-*-encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import sys
import traceback


session = requests.Session()

def getWeather(content):
	try:
		n = content.index(u"天气")
		city = content[0:n]
		area = city
		url = 'http://www.baidu.com/s?wd=' + urllib.quote((city+u"天气").encode("utf-8"))
		print(url)
		req = session.get(url)
		soup = BeautifulSoup(req.text,'html.parser')
		date = soup.find(attrs={'class':'op_weather4_twoicon_date'}).get_text().strip()


		try:
			tempNumber = soup.find(attrs={'class':'op_weather4_twoicon_shishi_title'}).get_text().strip()
			tempSup = soup.find(attrs={'class':'op_weather4_twoicon_shishi_sup'}).get_text().strip()
			tempSub = soup.find(attrs={'class':'op_weather4_twoicon_shishi_sub'}).get_text().strip()
			weatherReportNow = date + "\n" + tempNumber + tempSup + "  " + tempSub
			#print(weatherReportNow)
		except:
			pass

		dayTemp = soup.find(attrs={'class':'op_weather4_twoicon_temp'}).get_text().strip()
		dayWea = soup.find(attrs={'class':'op_weather4_twoicon_weath'}).get_text().strip()
		dayWind = soup.find(attrs={'class':'op_weather4_twoicon_wind'}).get_text().strip()
		try:
			dayQuailty = soup.find(attrs={'class':'op_weather4_twoicon_realtime_quality_wrap'}).span.span.get_text().strip()
		except:
			dayQuailty = ''
		weatherReportDay = city + "\n" + date + "\n" + dayTemp + "  " + dayWea + "," + dayWind + u",空气质量指数" + dayQuailty
		voiceReport = weatherReportDay.replace(u"~",u"至").replace(u"℃",u"度")
		return voiceReport
	except Exception, e:
		print Exception, ":", e
		traceback.print_exc()
		print("获取"+content+"失败")
		return ""

