#Example of using the response value when retrieving a list of liked songs

def get_first_song_name(song):
    return song['items'][0]['track']['name']

def get_song_names(songs):
    return [song['track']['name'] for song in songs['items']]