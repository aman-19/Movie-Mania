import requests
from lxml import html
import re

movies = []

for page in range(200):
	start = page*50+1
	url = "https://www.imdb.com/search/title?title_type=feature&start=" + str(start)
	response = requests.get(url)

	tree = html.fromstring(response.content)
	for i in range(1,51):
		print("----"+str(i + start -1 )+"-----")
		xPathSelector = '//*[@id="main"]/div/div[3]/div/div['+str(i)+']/div[3]/h3/span[2]'
		temp = tree.xpath(xPathSelector)
		try:
			year = temp[0].text_content().strip('()')
			z = re.match(re.compile('.*(\d\d\d\d)'),year)
			year = z.groups()[0].strip()
			print(year)
			if int(year)>2019:
				continue
		except:
			continue

		xPathSelector = '//*[@id="main"]/div/div[3]/div/div['+str(i)+']/div[3]/h3/a'

		try:
			temp = tree.xpath(xPathSelector)
			movie = temp[0].text_content()
			print(movie)
		except:
			continue	

		xPathSelector = '//*[@id="main"]/div/div[3]/div/div['+str(i)+']/div[3]/div/div[1]/strong'
		temp = tree.xpath(xPathSelector)
		try:
			rating = temp[0].text_content() 
			print(rating)
		except:
			continue

		xPathSelector = '//*[@id="main"]/div/div[3]/div/div['+str(i)+']/div[3]/p[3]'

		temp = tree.xpath(xPathSelector)
		# print(temp)
		stars = temp[0].text_content()
		# print(stars)
		# print(stars)
		z = re.match(re.compile('.*Stars?:(.*)', re.DOTALL),str(stars))
		try:
			stars = (z.groups()[0]).strip().split('\n')
			stars = [star.strip(', ') for star in stars]
			print(stars)
			stars = '*'.join(stars)
		except:
			stars = 'None'
		movies.append([movie, year, rating, stars])

with open("moviesList.csv", "w") as file:
	for movieInfo in movies:
		file.write('\t'.join(movieInfo)+"\n")
	file.close()