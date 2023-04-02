import os,sys,requests,bs4
from bs4 import BeautifulSoup

url = "https://jadwalnonton.com/bioskop/di-purwokerto/cgv-rita-supermall-purwokerto-2.html"



req = requests.get(url)
shoup = BeautifulSoup(req.text, 'html.parser')
items = shoup.findAll('div', 'col-sm-10 sched_desc')
os.system("cls")
print(" [!] LIST FILM CGV PURWOKERTO\n ")
for i in items:
    namaFilm = i.find("a").text
    umurTerpenuhi = i.find("span").text
    genre = i.find("p").text
    genre = genre.replace(" - ", "\n Durasi: ")
    studio = i.find("span", "showgroup").text
    jamTayang = i.find("li").text
    htm = i.find("span","htm").text
    htm = htm.replace("Tiket", "")
    print(" ###################")
    print(f" JUDUL: {namaFilm}")
    print(f" UMUR: {umurTerpenuhi}")
    print(f" GENRE: {genre}")
    print(f" STUDIO: {studio}")
    print(f" JAM TAYANG: {jamTayang}")
    print(f" HARGA TIKET:{htm}")
    print(" ###################\n")





