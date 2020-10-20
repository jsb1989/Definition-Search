import requests
from bs4 import BeautifulSoup

wikipage='https://en.wikipedia.org/wiki/'
dictionary='https://www.dictionary.com/browse/'
search=input("Enter what you would like to search:")

URL=dictionary+search

page=requests.get(URL)
dictionarysoup=BeautifulSoup(page.content,'html.parser')
while True:
	try:
		definition=dictionarysoup.find('div',attrs={"value":"1"})
		definition_text=definition.get_text()
		print("Dictionary Definition: ")
		print("- "+definition_text)
		break
	except AttributeError:
		print("Not a valid word for the dictionary, please re-enter again correctly or try another word")
		break

while True:
	try:
		definition=dictionarysoup.find('div',attrs={"value":"2"})
		definition_text=definition.get_text()
		print("- "+definition_text)
		break
	except AttributeError:
		break
