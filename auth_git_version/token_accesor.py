import base64
CL_ID = "client_id"
CL_SCRT = "client_secret"

#can find those on spotify api website.

URL =  'https://accounts.spotify.com/api/token'

import requests

body = {
    'code': "you can take this code from auth_changer file",
    'redirect_uri': "uri",
    'grant_type': 'authorization_code'
}

auth_header = base64.b64encode(f"{CL_ID}:{CL_SCRT}".encode()).decode()

headers = {
    'Authorization': f'Basic {auth_header}'
}

response = requests.post(url=URL,headers=headers, data=body)

if response.status_code == 200:
    token = response.json()
    print(token)
else:
    print(f"Error: {response.status_code}")
    print(response.raise_for_status())

#token accessor
