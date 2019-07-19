import bs4 as bs
import lxml
import urllib.request
import pandas as pd
from pandas import DataFrame
import numpy as np


### Scraping the city names
sauce = urllib.request.urlopen('https://karki23.github.io/Weather-Data/assignment.html').read()
srccode = bs.BeautifulSoup(sauce,'lxml')
ul_tags = srccode.find_all('ul')[0]
list_of_cities = ul_tags.find_all('li')
html_city_tags = []


for city in list_of_cities:
	x = city.text
	x  = x.replace(" ","")
	html_city_tags.append(x)

keys = []
data = {}
l =[]






for counter in range(49):
	url = 'https://karki23.github.io/Weather-Data/' + html_city_tags[counter] + '.html'
	print(counter)

	### Scraping the table from given url

	sauce = urllib.request.urlopen(url).read()
	srccode = bs.BeautifulSoup(sauce,'lxml')
	table = srccode.find_all('table')[0]
	rows = table.find_all('tr')


	### All rows appended to l
	for i in range(0,len(rows)):
	    for index, cell in enumerate(rows[i]):
	        if index %2 != 0 and index <=47: ###Appending only relevant cell boxes, not'\n' tags
	            l.append(cell.text)





	### Each row is a sublist of l,
	### hence create a 'list of rows'

	list_of_rows = [l[i:i+24] for i in range(0,len(l),24)]
	tuple_of_columns = list(zip(*list_of_rows))



	### Create a dictionary that is used in making csv
	for i in range(24):
	    data.update({tuple_of_columns[i][0]:tuple_of_columns[i][1:]})



### Creating csv with pandas for entire dataset
df = DataFrame(data, columns = list_of_rows[0])
df = df.sample(frac=1).reset_index(drop=True)
export_csv = df.to_csv (r'D:\Projects\PESU_IO_SUMMER\Final_Assignment\Datasets\city_details.csv', index = None, header=True)




"""
### Creating CSV for test and training

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]


export_csv = train.to_csv (r'D:\Projects\PESU_IO_SUMMER\Final_Assignment\Datasets\city_details_train.csv', index = None, header=True)
export_csv = test.to_csv (r'D:\Projects\PESU_IO_SUMMER\Final_Assignment\Datasets\city_details_test.csv', index = None, header=True)
"""



