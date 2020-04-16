import requests
from bs4 import BeautifulSoup

# Requests
r = requests.get("https://www.otempo.pt/porto.html", {"User-agent": "XY"})
r_1 = requests.get("https://www.otempo.pt/funchal.html", {"User-agent":"XY"})
r_2 = requests.get("https://www.otempo.pt/evora.html", {"User-agent":"XY"})
r_3 = requests.get("https://www.otempo.pt/braga.html", {"User-agent":"XY"})
r_4 = requests.get("https://www.otempo.pt/amadora.html", {"User-agent":"XY"})
r_5 = requests.get("https://www.otempo.pt/castelo-branco.html", {"User-agent":"XY"})
r_6 = requests.get("https://www.otempo.pt/leiria.html",{"User-agent":"XY"})
r_7 = requests.get("https://www.otempo.pt/montemor-o-novo.html", {"User-agent":"XY"})
r_8 = requests.get("https://www.otempo.pt/portalegre.html", {"User-agent":"XY"})
r_9 = requests.get("https://www.otempo.pt/queluz.html", {"User-agent":"XY"})
r_10 = requests.get("https://www.otempo.pt/setubal.html", {"User-agent":"XY"})
r_11 = requests.get("https://www.otempo.pt/vila-real.html", {"User-agent":"XY"})
r_12 = requests.get("https://www.otempo.pt/amora.html", {"User-agent":"XY"})
r_13 = requests.get("https://www.otempo.pt/braganca.html", {"User-agent":"XY"})
r_14 = requests.get("https://www.otempo.pt/coimbra.html", {"User-agent":"XY"})
r_15 = requests.get("https://www.otempo.pt/guarda.html", {"User-agent":"XY"})
r_16 = requests.get("https://www.otempo.pt/lisboa.html", {"User-agent":"XY"})
r_17 = requests.get("https://www.otempo.pt/ponta-delgada.html", {"User-agent":"XY"})
r_18 = requests.get("https://www.otempo.pt/portimao.html", {"User-agent":"XY"})
r_19 = requests.get("https://www.otempo.pt/santarem.html", {"User-agent":"XY"})
r_20 = requests.get("https://www.otempo.pt/viana-do-castelo.html", {"User-agent":"XY"})
r_21 = requests.get("https://www.otempo.pt/viseu.html", {"User-agent":"XY"})
r_22 = requests.get("https://www.otempo.pt/aveiro.html", {"User-agent":"XY"})
r_23 = requests.get("https://www.otempo.pt/cacem.html", {"User-agent":"XY"})
r_24 = requests.get("https://www.otempo.pt/faro.html", {"User-agent":"XY"})
r_25 = requests.get("https://www.otempo.pt/guimaraes.html", {"User-agent":"XY"})
r_26 = requests.get("https://www.otempo.pt/monsanto.html", {"User-agent":"XY"})
r_27 = requests.get("https://www.otempo.pt/ponte-de-lima.html", {"User-agent":"XY"})
r_28 = requests.get("https://www.otempo.pt/sequeira.html", {"User-agent":"XY"})
r_29 = requests.get("https://www.otempo.pt/vila-nova-de-gaia.html", {"User-agent":"XY"})



# Contents
content = r.content
content_1 = r_1.content
content_2 = r_2.content
content_3 = r_3.content
content_4 = r_4.content
content_5 = r_5.content
content_6 = r_6.content
content_7 = r_7.content
content_8 = r_8.content
content_9 = r_9.content
content_10 = r_10.content
content_11 = r_11.content
content_12 = r_12.content
content_13 = r_13.content
content_14 = r_14.content
content_15 = r_15.content
content_16 = r_16.content
content_17 = r_17.content
content_18 = r_18.content
content_19 = r_19.content
content_20 = r_20.content
content_21 = r_21.content
content_22 = r_22.content
content_23 = r_23.content
content_24 = r_24.content
content_25 = r_25.content
content_26 = r_26.content
content_27 = r_27.content
content_28 = r_28.content
content_29 = r_29.content

soup = BeautifulSoup(content, "html.parser")
soup_1 = BeautifulSoup(content_1, "html.parser")
soup_2 = BeautifulSoup(content_2, "html.parser")
soup_3 = BeautifulSoup(content_3, "html.parser")
soup_4 = BeautifulSoup(content_4, "html.parser")
soup_5 = BeautifulSoup(content_5, "html.parser")
soup_6 = BeautifulSoup(content_6, "html.parser")
soup_7 = BeautifulSoup(content_7, "html.parser")
soup_8 = BeautifulSoup(content_8, "html.parser")
soup_9 = BeautifulSoup(content_9, "html.parser")
soup_10 = BeautifulSoup(content_10, "html.parser")
soup_11 = BeautifulSoup(content_11, "html.parser")
soup_12 = BeautifulSoup(content_12, "html.parser")
soup_13 = BeautifulSoup(content_13, "html.parser")
soup_14 = BeautifulSoup(content_14, "html.parser")
soup_15 = BeautifulSoup(content_15, "html.parser")
soup_16 = BeautifulSoup(content_16, "html.parser")
soup_17 = BeautifulSoup(content_17, "html.parser")
soup_18 = BeautifulSoup(content_18, "html.parser")
soup_19 = BeautifulSoup(content_19, "html.parser")
soup_20 = BeautifulSoup(content_20, "html.parser")
soup_21 = BeautifulSoup(content_21, "html.parser")
soup_22 = BeautifulSoup(content_22, "html.parser")
soup_23 = BeautifulSoup(content_23, "html.parser")
soup_24 = BeautifulSoup(content_24, "html.parser")
soup_25 = BeautifulSoup(content_25, "html.parser")
soup_26 = BeautifulSoup(content_26, "html.parser")
soup_27 = BeautifulSoup(content_27, "html.parser")
soup_28 = BeautifulSoup(content_28, "html.parser")
soup_29 = BeautifulSoup(content_29, "html.parser")


all = soup.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_1 = soup_1.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_2 = soup_2.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_3 = soup_3.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_4 = soup_4.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_5 = soup_5.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_6 = soup_6.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_7 = soup_7.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_8 = soup_8.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_9 = soup_9.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_10 = soup_10.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_11 = soup_11.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_12 = soup_12.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_13 = soup_13.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_14 = soup_14.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_15 = soup_15.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_16 = soup_16.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_17 = soup_17.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_18 = soup_18.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_19 = soup_19.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_20 = soup_20.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_21 = soup_21.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_22 = soup_22.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_23 = soup_23.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_24 = soup_24.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_25 = soup_25.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_26 = soup_26.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_27 = soup_27.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_28 = soup_28.find_all("span", {"class": "m_table_weather_day_max_temp"})
all_29 = soup_29.find_all("span", {"class": "m_table_weather_day_max_temp"})


# Get the text
today_temp = all[0].find_all("span")[0].text
today_temp_1 = all_1[0].find_all("span")[0].text
today_temp_2 = all_2[0].find_all("span")[0].text
today_temp_3 = all_3[0].find_all("span")[0].text
today_temp_4 = all_4[0].find_all("span")[0].text
today_temp_5 = all_5[0].find_all("span")[0].text
today_temp_6 = all_6[0].find_all("span")[0].text
today_temp_7 = all_7[0].find_all("span")[0].text
today_temp_8 = all_8[0].find_all("span")[0].text
today_temp_9 = all_9[0].find_all("span")[0].text
today_temp_10 = all_10[0].find_all("span")[0].text
today_temp_11 = all_11[0].find_all("span")[0].text
today_temp_12 = all_12[0].find_all("span")[0].text
today_temp_13 = all_13[0].find_all("span")[0].text
today_temp_14 = all_14[0].find_all("span")[0].text
today_temp_15 = all_15[0].find_all("span")[0].text
today_temp_16 = all_16[0].find_all("span")[0].text
today_temp_17 = all_17[0].find_all("span")[0].text
today_temp_18 = all_18[0].find_all("span")[0].text
today_temp_19 = all_19[0].find_all("span")[0].text
today_temp_20 = all_20[0].find_all("span")[0].text
today_temp_21 = all_21[0].find_all("span")[0].text
today_temp_22 = all_22[0].find_all("span")[0].text
today_temp_23 = all_23[0].find_all("span")[0].text
today_temp_24 = all_24[0].find_all("span")[0].text
today_temp_25 = all_25[0].find_all("span")[0].text
today_temp_26 = all_26[0].find_all("span")[0].text
today_temp_27 = all_27[0].find_all("span")[0].text
today_temp_28 = all_28[0].find_all("span")[0].text
today_temp_29 = all_29[0].find_all("span")[0].text


# Clear the specials characters
today = ''.join(e for e in today_temp if e.isalnum())
today_1 = ''.join(e for e in today_temp_1 if e.isalnum())
today_2 = ''.join(e for e in today_temp_2 if e.isalnum())
today_3 = ''.join(e for e in today_temp_3 if e.isalnum())
today_4 = ''.join(e for e in today_temp_4 if e.isalnum())
today_5 = ''.join(e for e in today_temp_5 if e.isalnum())
today_6 = ''.join(e for e in today_temp_6 if e.isalnum())
today_7 = ''.join(e for e in today_temp_7 if e.isalnum())
today_8 = ''.join(e for e in today_temp_8 if e.isalnum())
today_9 = ''.join(e for e in today_temp_9 if e.isalnum())
today_10 = ''.join(e for e in today_temp_10 if e.isalnum())
today_11 = ''.join(e for e in today_temp_11 if e.isalnum())
today_12 = ''.join(e for e in today_temp_12 if e.isalnum())
today_13 = ''.join(e for e in today_temp_13 if e.isalnum())
today_14 = ''.join(e for e in today_temp_14 if e.isalnum())
today_15 = ''.join(e for e in today_temp_15 if e.isalnum())
today_16 = ''.join(e for e in today_temp_16 if e.isalnum())
today_17 = ''.join(e for e in today_temp_17 if e.isalnum())
today_18 = ''.join(e for e in today_temp_18 if e.isalnum())
today_19 = ''.join(e for e in today_temp_19 if e.isalnum())
today_20 = ''.join(e for e in today_temp_20 if e.isalnum())
today_21 = ''.join(e for e in today_temp_21 if e.isalnum())
today_22 = ''.join(e for e in today_temp_22 if e.isalnum())
today_23 = ''.join(e for e in today_temp_23 if e.isalnum())
today_24 = ''.join(e for e in today_temp_24 if e.isalnum())
today_25 = ''.join(e for e in today_temp_25 if e.isalnum())
today_26 = ''.join(e for e in today_temp_26 if e.isalnum())
today_27 = ''.join(e for e in today_temp_27 if e.isalnum())
today_28 = ''.join(e for e in today_temp_28 if e.isalnum())
today_29 = ''.join(e for e in today_temp_29 if e.isalnum())


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

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_6 + "," + "Leiria,39.7495,-8.8077\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_7 + "," + "Montemor o Velho,40.1748,-8.6827\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_8 + "," + "Portalegre,39.2967,-7.4285\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_9 + "," + "Queluz,38.7574,-9.2587\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_10 + "," + "Setubal,38.5260,-8.8909\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_11 + "," + "Vila Real,41.3010,-7.7422\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_12 + "," + "Amora,38.6201,-9.1345\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_13 + "," + "Braganca,41.8061,-6.7567\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_14 + "," + "Coimbra,40.2033,-8.4103\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_15 + "," + "Guarda,40.5308,-7.2221\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_16 + "," + "Lisboa,38.7223,-9.1393\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_17 + "," + "Ponta de Delgada,37.7494,-25.6649\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_18 + "," + "Portimão,37.1362,-8.5377\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_19 + "," + "Santarem,39.2367,-8.6860\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_20 + "," + "Viana do Castelo,41.6918,-8.8344\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_21 + "," + "Viseu,40.6566,-7.9125\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_22 + "," + "Aveiro,40.6405,-8.6538\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_23 + "," + "Cacem,38.7680,-9.2988\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_24 + "," + "Faro,37.0194,-7.9304\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_25 + "," + "Guimaraes,41.4425,-8.2918\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_26 + "," + "Monsanto,40.0389,-7.1151\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_27 + "," + "Ponte de Lima,41.7647,-8.5827\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_28 + "," + "Sequeira,41.5277,-8.4717\n")
f.close()

f = open("temps/todaysTemMax.txt", "a+")
f.write(today_29 + "," + "Vila Nova de Gaia,41.1239,-8.6118\n")
f.close()
#f = open("todaysTemMax.txt", "a+")
#f.write(today)
#f.close()

# print(all)