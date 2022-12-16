from bs4 import BeautifulSoup
import lxml
import requests

with open("calc.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
# print("hi")
# #IET Lucknow.html
# print(soup.find_all(name="td"))

response = requests.get("https://www.collegepravesh.com/engineering-colleges/iet-lucknow/#courses")
cpwebpage= response