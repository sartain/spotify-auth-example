import pytest
from modules.songs import get_first_song_name, get_song_names

#Contains an example list of song names at the same level as endpoint request
#This is an example of adding unit tests based on response before making API call

example_song_name_list = {
    "items": [
        {
            "track": {
                "name": "a"
            }
        },
        {
            "track": {
                "name": "b"
            }
        },
        {
            "track": {
                "name": "c"
            }
        },
        {
            "track": {
                "name": "d"
            }
        },
        {
            "track": {
                "name": "e"
            }
        },
        {
            "track": {
                "name": "f"
            },
        }
    ]
}

example_track = {
    "items": [{
        "track": {
            "album": {
            "album_type": "album",
            "total_tracks": 9,
            "external_urls": {
                "spotify": "https://open.spotify.com/album/680ImGmXgTLzEAVHEe7Zb6"
            },
            "href": "https://api.spotify.com/v1/albums/680ImGmXgTLzEAVHEe7Zb6",
            "id": "680ImGmXgTLzEAVHEe7Zb6",
            "images": [
                {
                "url": "https://i.scdn.co/image/ab67616d0000b273b2b15f0d83d7f5b82f7af279",
                "height": 640,
                "width": 640
                },
                {
                "url": "https://i.scdn.co/image/ab67616d00001e02b2b15f0d83d7f5b82f7af279",
                "height": 300,
                "width": 300
                },
                {
                "url": "https://i.scdn.co/image/ab67616d00004851b2b15f0d83d7f5b82f7af279",
                "height": 64,
                "width": 64
                }
            ],
            "name": "First Light",
            "release_date": "1982",
            "release_date_precision": "year",
            "type": "album",
            "uri": "spotify:album:680ImGmXgTLzEAVHEe7Zb6",
            "artists": [
                {
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/5qm3bAgsYq5aBOymqkM4gG"
                },
                "href": "https://api.spotify.com/v1/artists/5qm3bAgsYq5aBOymqkM4gG",
                "id": "5qm3bAgsYq5aBOymqkM4gG",
                "name": "Makoto Matsushita",
                "type": "artist",
                "uri": "spotify:artist:5qm3bAgsYq5aBOymqkM4gG"
                }
            ],
            "is_playable": True
            },
            "artists": [
            {
                "external_urls": {
                "spotify": "https://open.spotify.com/artist/5qm3bAgsYq5aBOymqkM4gG"
                },
                "href": "https://api.spotify.com/v1/artists/5qm3bAgsYq5aBOymqkM4gG",
                "id": "5qm3bAgsYq5aBOymqkM4gG",
                "name": "Makoto Matsushita",
                "type": "artist",
                "uri": "spotify:artist:5qm3bAgsYq5aBOymqkM4gG"
            }
            ],
            "disc_number": 1,
            "duration_ms": 271950,
            "explicit": False,
            "external_ids": {
            "isrc": "JPWP02070106"
            },
            "external_urls": {
            "spotify": "https://open.spotify.com/track/6A9YFkei6zWfPSxWxlBecY"
            },
            "href": "https://api.spotify.com/v1/tracks/6A9YFkei6zWfPSxWxlBecY",
            "id": "6A9YFkei6zWfPSxWxlBecY",
            "is_playable": True,
            "linked_from": {
            "external_urls": {
                "spotify": "https://open.spotify.com/track/18kqtvnINk0hDD1Tzdsf1q"
            },
            "href": "https://api.spotify.com/v1/tracks/18kqtvnINk0hDD1Tzdsf1q",
            "id": "18kqtvnINk0hDD1Tzdsf1q",
            "type": "track",
            "uri": "spotify:track:18kqtvnINk0hDD1Tzdsf1q"
            },
            "name": "September Rain - 2020 Remaster",
            "popularity": 53,
            "preview_url": "https://p.scdn.co/mp3-preview/baf38c12ba6e210bfe346933e5f3fc2c9f76d428?cid=0b297fa8a249464ba34f5861d4140e58",
            "track_number": 10,
            "type": "track",
            "uri": "spotify:track:6A9YFkei6zWfPSxWxlBecY",
            "is_local": False
        }
    }]
}

def test_get_song_name():
    expected_song_name = "September Rain - 2020 Remaster"
    actual_song_name = get_first_song_name(example_track)
    assert expected_song_name == actual_song_name

def test_get_song_list():
    expected_song_names = ['a','b','c','d','e','f']
    actual_song_names = get_song_names(example_song_name_list)
    assert expected_song_names == actual_song_names