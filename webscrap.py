from bs4 import BeautifulSoup
import requests

req = requests.get('https://stackoverflow.com/questions/tagged/python')
soup = BeautifulSoup(req.content,'html.parser')

res = []

for i in soup.find_all("a",class_="question-hyperlink",href=True):
        res.append(i['href'])
for ques in res:
        print(ques.replace("https://",""))
        print('-'*20)