from bs4 import BeautifulSoup
import requests

URL="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
respond=requests.get(URL)
website_html=respond.text

soup=BeautifulSoup(website_html,"html.parser")
all_movies=soup.find_all(name="h3")

movies_title=[movie.getText() for movie in all_movies]

movies = movies_title[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for item in movies:

        if item.strip():
            file.write(f"{item}\n")

print(f"Done! {len(movies)} movies have been written to movies.txt")