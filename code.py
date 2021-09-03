'''
ICE-1 9/3/2021
Program to tokenize a web page about SpaceX.
Author(s): Sudheer Bandaru
'''
import urllib.request
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
nltk.download('stopwords')

# Request to the SpaceX wikipedia page
response = urllib.request.urlopen('https://www.spacex.com/')
html = response.read()

# Cleanly traverse HTML with beautiful soup
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]

# Create a list of clean tokens
clean_tokens = tokens[:]

# Obtain stop words for english text
sr = stopwords.words('english')

for token in tokens:
if token in stopwords.words('english'):
clean_tokens.remove(token)

# Get word frequency using Natural Language Toolkit (stored as a dictionary from word to frequency)
frequ = nltk.FreqDist(clean_tokens)

# Restricting the words occurred less than 5 times
for key,val in frequ.items():
  if val > 5:
print(str(key)+ ':' + str(val))

# Use matplotlib to show a graph of the frequency (only including first 10 items
frequ.plot(10,cumulative=False)

#Creating pie chart for the frequency Distribution
h = nltk.FreqDist({key:val for key,val in frequ.items() if val > 60})
plt.pie(h.values(),explode=None,radius=2,labels=h.keys(),shadow=False)         
plt.show()
