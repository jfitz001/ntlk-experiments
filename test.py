import nltk
from nltk.tokenize import word_tokenize

from bs4 import BeautifulSoup as bs
import requests

#websites for parsing
googlenews = "https://www.google.com/search?rlz=1C1CHWA_enUS628US628&q=tesla+news&tbm=nws&source=univ&tbo=u&sa=X&ved=2ahUKEwirtffb6frfAhXEnuAKHcA9Ba0Qt8YBKAF6BAgAEC4&biw=1920&bih=943"
tesla = "https://www.google.com/search?q=tesla+news&rlz=1C1CHWA_enUS628US628&source=lnms&sa=X&ved=0ahUKEwiT6a_e6frfAhXCnuAKHUE0B0sQ_AUICSgA&biw=979&bih=943&dpr=1"
#array to use in for loop
websites = [googlenews, tesla]

for x in websites:

 page = requests.get(x)

 soup = bs(page.content, "html.parser")

 results = soup.find_all("div", {"class": "st"})
 results2 = soup.find_all ("span", {"class": "st"})
 x = 0
 key_array = [i for i in range(10)]
 for key in results:
     print(key.text)
     x = x + 1

print('\n')
 
for key in results2:
     print(key.text)    


