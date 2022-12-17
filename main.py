from bs4 import BeautifulSoup
import lxml
import requests

with open("calc.html") as file:
    contents = file.read()

#soup = BeautifulSoup(contents, "lxml")
# print("hi")
# #IET Lucknow.html
# print(soup.find_all(name="td"))

response = requests.get("https://www.abplive.com/live-tv")
flipkartwebpage= response.text
soup = BeautifulSoup(flipkartwebpage,"lxml")
courses = soup.find(name="p", class_="fz18")
print(courses.getText())
#<div class="_3YgSsQ" style="width: 410px;"><div class="_PjFpB" data-tracking-id="10"><a title="Boat" target="" class="i5i9oO" href="/boat-aavante-bar-1600d-120-w-bluetooth-soundbar/p/itmdd0aa86f0bf12?pid=ACCG7632H2KAMQAB&amp;otracker=hp_nativeads_Featured%2BBrands_1_10.nativeAdCard.NATIVEADS_Boat_JVBXLPYMU7F1"><div class="_1OkOw1"><div class="_1bEAQy _2iN8uD" style="width: 400px; height: 215px;"><img class="_2OHU_q aA9eLq" alt="Boat" srcset="https://rukminim1.flixcart.com/fk-p-flap/656/352/image/5ac6967ff0e4c10d.jpeg?q=70 2x, https://rukminim1.flixcart.com/fk-p-flap/1312/704/image/5ac6967ff0e4c10d.jpeg?q=70 1x" src="https://rukminim1.flixcart.com/fk-p-flap/1312/704/image/5ac6967ff0e4c10d.jpeg?q=70" data-tkid="A_58898462-e1fb-47e4-b137-9c21b7e3a9f3_10.JVBXLPYMU7F1"><img class="kJjFO0 _3DIhEh" src="https://rukminim1.flixcart.com/fk-p-flap/50/50/image/5ac6967ff0e4c10d.jpeg?q=50" alt="Boat"></div></div></a></div></div>
#_37K3-p