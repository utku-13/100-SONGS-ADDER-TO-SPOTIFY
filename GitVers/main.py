from web_scraper_oop import WebScraper
from song_id_finder_oop import FindId
from song_adder_oop import SongAdder

get_date = input("Give me a date!(in this format:2004-12-18)\nMust be after 2004-00-00!!")

w = WebScraper()

list_encoded_names = w.get_encoded_name_list(f"https://www.billboard.com/charts/hot-100/{get_date}/")

f = FindId()

list_ids = f.find_id(list_encoded_names)

s = SongAdder()

s.add_songs(list_ids)

