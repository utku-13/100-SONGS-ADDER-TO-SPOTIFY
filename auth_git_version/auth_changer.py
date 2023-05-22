from flask import Flask, redirect, request
import random
import string
import urllib.parse

client_id = "client_id"
redirect_uri = 'uri'

app = Flask(__name__)

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

@app.route('/callback')
def callback():
    code = request.args.get('code')
    # Use 'code' to get an access token, typically you send a POST request to Spotify's /api/token endpoint.
    # Implementation of this depends on how you handle HTTP requests (requests, httplib, etc.)
    # Also handle the case when 'code' is None
    return "Received code: " + code

@app.route('/login')
def login():
    state = generate_random_string(16)
    scope = 'playlist-modify-private playlist-modify-public'
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'scope': scope,
        'redirect_uri': redirect_uri,
        'state': state
    }

    url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)

    return redirect(url)

if __name__ == "__main__":
    app.run(port=8888)
