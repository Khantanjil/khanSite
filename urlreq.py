import requests
from bs4 import BeautifulSoup

# Requests
r = requests.get("https://www.otempo.pt/porto.html", {"User-agent": "XY"})
r_1 = requests.get("https://www.otempo.pt/funchal.html", {"User-agent":"XY"})
r_2 = requests.get("https://www.otempo.pt/evora.html", {"User-agent":"XY"})
r_3 = requests.get("https://www.otempo.pt/braga.html", {"User-agent":"XY"})
r_4 = requests.get("https://www.otempo.pt/amadora.html", {"User-agent":"XY"})
r_5 = requests.get("https://www.otempo.pt/castelo-branco.html", {"User-agent":"XY"})


# Contents
content = r.content
content_1 = r_1.content
content_2 = r_2.content
content_3 = r_3.content
content_4 = r_4.content
content_5 = r_5.content

soup = BeautifulSoup(content, "html.parser")
soup_1 = BeautifulSoup(content_1, "html.parser")
soup_2 = BeautifulSoup(content_2, "html.parser")
soup_3 = BeautifulSoup(content_3, "html.parser")
soup_4 = BeautifulSoup(content_4, "html.parser")
soup_5 = BeautifulSoup(content_5, "html.parser")

all = soup.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_1 = soup_1.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_2 = soup_2.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_3 = soup_3.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_4 = soup_4.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_5 = soup_5.find_all("span", {"class": "m_table_weather_day_max_temp"})

# Get the text
today_temp = all[0].find_all("span")[0].text
today_temp_1 = all_1[0].find_all("span")[0].text
today_temp_2 = all_2[0].find_all("span")[0].text
today_temp_3 = all_3[0].find_all("span")[0].text
today_temp_4 = all_4[0].find_all("span")[0].text
today_temp_5 = all_5[0].find_all("span")[0].text

# Clear the specials characters
today = ''.join(e for e in today_temp if e.isalnum())
today_1 = ''.join(e for e in today_temp_1 if e.isalnum())
today_2 = ''.join(e for e in today_temp_2 if e.isalnum())
today_3 = ''.join(e for e in today_temp_3 if e.isalnum())
today_4 = ''.join(e for e in today_temp_4 if e.isalnum())
today_5 = ''.join(e for e in today_temp_5 if e.isalnum())

# Write to the data file
f = open("temps/todaysTemMax.txt", "a+")
f.truncate(0)
f.write("temperature,city,latitude,longitude\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_2 + "," + "Evora,38.5714,-7.9135\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_1 + "," + "Funchal,32.6669,-16.9241\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today + "," + "Porto,41.1579,-8.6291\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_3 + "," + "Braga,41.5454,-8.4265\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_4 + "," + "Amadora,38.7578,-9.2245\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_5 + "," + "Castelo Branco,39.8031,-7.4598\n")
f.close()
#f = open("todaysTemMax.txt", "a+")
#f.write(today)
#f.close()

# print(all)