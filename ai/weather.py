#-*-encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys



session = requests.Session()

def getWeather(area):
	try:
		url = 'http://www.baidu.com/s?wd=' + area + '天气'
		req = session.get(url)
		soup = BeautifulSoup(req.text,'html.parser')
		date = soup.find(attrs={'class':'op_weather4_twoicon_date'}).get_text().strip()
		print('【' + area + '天气】')

		try:
			tempNumber = soup.find(attrs={'class':'op_weather4_twoicon_shishi_title'}).get_text().strip()
			tempSup = soup.find(attrs={'class':'op_weather4_twoicon_shishi_sup'}).get_text().strip()
			tempSub = soup.find(attrs={'class':'op_weather4_twoicon_shishi_sub'}).get_text().strip()
			weatherReportNow = date + "\n" + tempNumber + tempSup + "  " + tempSub
			print(weatherReportNow)
		except:
			pass

		dayTemp = soup.find(attrs={'class':'op_weather4_twoicon_temp'}).get_text().strip()
		dayWea = soup.find(attrs={'class':'op_weather4_twoicon_weath'}).get_text().strip()
		dayWind = soup.find(attrs={'class':'op_weather4_twoicon_wind'}).get_text().strip()
		try:
			dayQuailty = soup.find(attrs={'class':'op_weather4_twoicon_realtime_quality_wrap'}).span.span.get_text().strip()
		except:
			dayQuailty = ''
		weatherReportDay = date + "\n" + dayTemp + "  " + dayWea + "," + dayWind + u",空气质量指数" + dayQuailty
		print(weatherReportDay)
		print('')
		return weatherReportDay
	except:
		print('失败')

