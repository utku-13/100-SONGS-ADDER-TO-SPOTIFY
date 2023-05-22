from bs4 import BeautifulSoup
import requests
from urllib.parse import quote


class WebScraper:
    def get_encoded_name_list(self, url_u_wanted):
        response = requests.get(url=url_u_wanted)

        web_page = response.text

        soup = BeautifulSoup(web_page,"html.parser")

        First_songs_title = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
        first_song = []
        for title in First_songs_title:
            first_song.append(title.getText())


        first_song_name = [song.strip() for song in first_song]


        titles = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
        song_list = []
        for title in titles:
            song_list.append(title.getText())


        song_names = [song.strip() for song in song_list]


        song_names.insert(0,first_song_name[0])

        #i got all the song names now we need to find ids.
        encoded_song_names = []
        for name in song_names:
            name = quote(name)
            encoded_song_names.append(name)
            
        return encoded_song_names