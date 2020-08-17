import requests
import json
from difflib import get_close_matches
from bs4 import BeautifulSoup
def wiki(x):
    link="https://en.wikipedia.org/wiki"+"/"+str(x)
    r=requests.get(link)
    c=r.content
    soup=BeautifulSoup(c,'html.parser')
    try:
        for i in range(10):
         all=soup.find_all("p")[i].text
         print(all)
    except:
        data = json.load(open("data.json", "r"))
        w=x.lower()
        print("Did you mean %s"%get_close_matches(w,data.keys()))
        for i in get_close_matches(w,data.keys()):
           print("Did you mean %s"%i)
           g=input("Enter Y if yes else N\n")
           if g=="Y":
               wiki(i)
               break

        else:
           print("Word doesnt exist")
n=input("Enter the word\n")
wiki(n)
