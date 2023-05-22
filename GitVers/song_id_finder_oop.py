import requests

class FindId:
    def find_id(self, song_encoded_names):
        all_ids = []
        for songs in song_encoded_names:
            url = f"https://api.spotify.com/v1/search?q=track:{songs}&type=track"

            headers = {
                "Authorization": "Bearer [auth_token]",
            }

            response = requests.get(url, headers=headers)

            # This will print the status code

            # This will print the json response
            json1 = response.json()["tracks"]["items"][0]["id"]
            all_ids.append(json1)
        return all_ids
            
        
        