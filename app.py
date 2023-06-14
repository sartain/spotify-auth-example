from flask import Flask, render_template, redirect, request
from modules.songs_backend import get_auth_params, initialize_state, request_token, get_liked_songs, refresh_token, invalid_state

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

"""
Example route to retrieve data.
In this example, upon a button click, a user's liked songs are retrieved.
"""
@app.route('/likedsongs')
def liked_songs():
    liked_songs = get_liked_songs()
    return render_template('redirect.html')

"""
Base this route on the callback URI.
After step 1 is completed, we are redirected here.
Check state variable matches existing, only complete step 2 if so.
"""
#Example is localhost:PORT/callback
@app.route('/callback')
def callback():
    if invalid_state(request.args.get('state')):
        redirect("/")
    code = request.args.get('code')
    request_token(code)
    return render_template('redirect.html')

"""
In example, clicking authorize button redirects here
If token exists, refresh token.
If not, complete step 1.
"""
@app.route('/authorize', methods=['GET'])
def authorize():
    if refresh_token():
        return render_template('redirect.html')
    else:
        initialize_state()
        params = get_auth_params()
        authorization_url = 'https://accounts.spotify.com/authorize'
        return redirect(authorization_url + '?' + '&'.join([f'{k}={v}' for k, v in params.items()]))

if __name__ == '__main__':
    app.run(host='localhost', port=8080)