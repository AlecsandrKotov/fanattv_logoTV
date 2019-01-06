# Скачиваем иконки с сайта http://fanat.tv/channels
import requests
from bs4 import BeautifulSoup
import os

REQUEST_STATUS_CODE = 200							#Константа запроса к сайту с ответом 200 (для проверки доступа к ресурсу)
folfer = "./logo/"									#путь к папке (начинаться должна с './' и в конце '/')
url_site = 'http://fanat.tv/channels'	 			#сайт с которого парсим иконки и имена каналов для них
response = requests.get(url_site)
html = response.content
soup = BeautifulSoup(html, 'lxml')
def download_logo():
	box = soup.find_all('div', class_='product')		#Ищем все теги 'DIV' где содержитсяназвание и иконка
	for i in box:
		p = i.find('p').text							#Получаем имя канала
		img_url = i.find('div').find('img').get('src')	#Получаем путь к иконке канала
		img_name = img_url[10:]							#Делаем срез 'images/tv/'' оставляем все после последнего '/'
		#img_raw = img_url[:4]							#Оставляем расширение файла 'png'
		x = img_name.find('.')							#Ищем знак точки и находим его значение от начала
		new = img_name[x:]								#делаем срез на основе данных выше (строка выше)
		new_img = p + new

		#print (p)										#имя с сайта
		#print (img_name)								#имя логотипа с сайта
		#print(new_img)									#новое имя для
		#print ('------------------------------')

		#Скачиваем иконки с сайта http://fanat.tv/channels
		if  os.path.isdir(folfer):							#проверяем существование папки
			url = 'http://fanat.tv/' + img_url				#Путь к иконкам на сайте
			patch = folfer + new_img						#Путь к папке и новое имя иконки логотипа
			send=requests.get(url)

			if send.status_code == REQUEST_STATUS_CODE:		#Получаем ответ от сайта 200 (REQUEST_STATUS_CODE = 200) тогда выполняемсохранение
				with open (patch,'wb') as f:
					f.write(send.content)
					print('Иконка - ' + new_img)
		else:

			os.mkdir(folfer)									#Создаем папку (путь в переменной 'folfer')
			print('Папка созданна - ' + folfer)	#Выводим путь папки
			download_logo()										#Запускаем функцию по новой
	print('Все файлы скачены!')


download_logo() #Запускаем функцию для скачивания логотипов с сайта http://fanat.tv/channels
