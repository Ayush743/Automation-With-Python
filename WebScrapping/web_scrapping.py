
from bs4 import BeautifulSoup
import requests
import smtplib


content=""
url="https://timesofindia.indiatimes.com/news"

response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
content=soup.find_all(class_="UreF0")
for text in content:
    for child_tag in text:
        child_tag.getText()
        print()
   
      



