# Spotify Authorization API template

A python example of the authorization flow in Spotify.
This can be used as a template to play around with the APIs.
This is not designed for production as the tokens are stored locally in a json file, and the flask web server is development.

## Requirements

- A spotify [app](https://developer.spotify.com/documentation/web-api/concepts/apps).
  - Client ID and Client Secret from the app.
  - Redirect URI from the app.
- Python

## Adding missing files and contents

- Create a .env file and fill out contents with:

  - `CLIENT_ID`
  - `CLIENT_SECRET`
  - `REDIRECT_URI`

- Create an empty config.json file

  - This will store the token values.
  - _This file is included in the git ignore to avoid publishing tokens._

## Setup

- Create virtual python environment

  - `python3 -m venv venv`

- Enter virtual environment

  - `source venv/bin/activate`

- Install dependencies

  - `pip install -r requirements.txt`
  - Any future dependencies, place in this file.

- Running tests

  - `pytest`

- Running application
  - `python app.py`
  - Navigate to `localhost:8080` or wherever you choose to run in `app.py` to view authorization

## How to use the template

This template has been setup to cover the authorization steps and make it simple to get started on using Spotify APIs.

There is an 'authorize' button which completes the authorization stages. Future clicks of the button will attempt to use the refresh token.
The official documentation for the authorization stages is [here](https://developer.spotify.com/documentation/web-api/tutorials/code-flow).

## Adding Spotify API calls

The authorization header, with the token, can be retrieved and used for future API requests via `songs_backend.py` method `get_token_headers`.

To use an endpoint which requires more permissions, update the [scope](https://developer.spotify.com/documentation/web-api/concepts/scopes) field found in `songs_backend.py` method `get_auth_params`.

An example Spotify API request is found in `songs_backend.py` method `get_liked_songs`.

To find and use more API endpoints look [here](https://developer.spotify.com/documentation/web-api).

Use `app.py` to enable the front-end to call the backend method and display the contents.
