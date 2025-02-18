import requests
from bs4 import BeautifulSoup

f=open("Automation-With-Python/WebScrapping/test.html","r")
html_doc=f.read()
soup=BeautifulSoup(html_doc,"html.parser")
# print(soup.title.string)
# print(soup.find_all("div")[1].string)
# print(soup.find_all("a"))

# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.getText())

# print(soup.find("div",class_="bleach").string)
# print(soup.find(id="naruto").string)

# print(soup.select("p.para"))
# print(soup.select("p#p"))
# print(soup.div.get("class"))

# for child in soup.find(class_="anime").children:
#     print(child.getText())

anime=soup.find(class_="anime")
anime.name="span"
anime["class"]="ani aki"


ul=soup.new_tag("ul")
nav=soup.new_tag("nav")
def list_tag(name):
    li=soup.new_tag("li")
    li.string=name
    ul.append(li)

list_tag("home")
list_tag("About")
list_tag("Contact us")
list_tag("Services")
nav.append(ul)
soup.html.body.insert(0,nav)
with open("new_test.html","w") as f:
    f.write(str(soup))
    f.close()

def has_content_attr(tag):
    return tag.has_attr("href")

results=soup.find_all(has_content_attr)
for result in results:
    print(result)
    print()
