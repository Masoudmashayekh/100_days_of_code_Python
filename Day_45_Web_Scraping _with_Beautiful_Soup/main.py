from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movies_list = [movie.getText() for movie in movies]
rev = movies_list[::-1]
print(rev)
with open("Movies.txt", mode="w") as file:
    for film in rev:
        contents = file.write(f"{film}\n")
