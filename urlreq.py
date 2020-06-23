import requests
from bs4 import BeautifulSoup
import pandas


portugal = ["porto", "funchal", "evora", "braga", "amadora", "castelo-branco", "leiria", "montemor-o-novo", "portalegre", "queluz",
		"setubal", "vila-real", "amora", "braganca", "coimbra", "guarda", "lisboa", "ponta-delgada", "portimao", "santarem", 
		"viana-do-castelo", "viseu", "aveiro", "cacem", "faro", "guimaraes", "monsanto", "ponte-de-lima", "vila-nova-de-gaia"]

lat = ["41.1579", "32.6669", "38.5714","41.5454","38.7578",
		"39.8197", "39.7495","38.6473","39.2967", "38.7574",
		"38.5260", "41.3010", "38.6201","41.8061","40.2033",
		"40.5308", "38.7223", "37.7394", "37.1362", "39.2367",
		"41.6918", "40.6566", "40.6405","38.7680","37.0194","41.4425",
		"40.0389", "41.7647", "41.1239"]

lon = ["-8.6291", "-16.9241", "-7.9135", "-8.4265", "-9.2245",
		"-7.4965", "-8.8077", "-8.2123", "-7.4285", "-9.2587",
		"-8.8909", "-7.7422", "-9.1345", "-6.7567", "-8.4103",
		"-7.2221", "-9.1393", "-25.6687", "-8.5377", "-8.6860",
		"-8.8345", "-7.9125","-8.6538", "-9.2988", "-7.9304",
		"-8.2918", "-7.1151", "-8.5827", "-8.6118"]
temps = []
for i in portugal:
	base_url = "https://www.otempo.pt/"
	r = requests.get(base_url+i+".html", headers={
		"user-agent":"XY"
		})
	content = r.content
	soup = BeautifulSoup(content, "html.parser")
	all = soup.find_all("span", {"class": "m_table_weather_day_max_temp"})
	today_temp = all[0].find_all("span")[0].text
	today = ''.join(e for e in today_temp if e.isalnum())
	temps.append(today)
	#print(temps)
	l = []
	for city, latitude, longitude in zip(portugal, lat, lon):
		d = {}
		d["City"] = city
		d["Latitude"] = latitude
		d["Longitude"] = longitude
		d["Temperature"] = today
		l.append(d)

df = pandas.DataFrame(l)
