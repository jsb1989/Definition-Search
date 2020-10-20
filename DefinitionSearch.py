import requests

wikipage='https://en.wikipedia.org/wiki/'
dictionary='https://www.dictionary.com/browse/'
dictionaryend='?s=t'
search=input("Enter what you would like to search:")

URL1=wikipage+search
URL2=dictionary+search+dictionaryend

page1=requests.get(URL1)
page2=requests.get(URL2)