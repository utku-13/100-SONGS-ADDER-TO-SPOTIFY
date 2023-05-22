import requests
import json
user_id = "user_id"
playlist_id = "playlist_id"
class SongAdder:
    def add_songs(self, song_id):
        playlist_id = "playlist_id"
        for id in song_id:
            url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
            headers = {
                'Authorization': 'Bearer [auth_token]',
                'Content-Type': 'application/json',
            }
            payload = {
                "uris": [f"spotify:track:{id}"],  # Replace with actual Spotify URI(s)
            }

            try:
                response = requests.post(url, headers=headers, data=json.dumps(payload))

                print(response.raise_for_status())
            except:
                print("unlcuky")