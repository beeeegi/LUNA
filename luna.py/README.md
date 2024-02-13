# This is the original LUNA code written in python

## Usage
### Installing Dependencies
`-` Run the following command to install the required dependencies
```
pip install -r requirements.txt
```
### Setting Up Environment Variables
`1.` Create a file named .env in the same directory as your script.

`2.` Inside the .env file, define the following environment variables:
```
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=your_spotify_redirect_uri
SPOTIPY_USERNAME=your_spotify_username
DISCORD_WEBHOOK_URL=your_discord_webhook_url
```
### Running and using LUNA
`1.` Run the following command in your terminal or command prompt
```
python main.py
```
`2.` LUNA will prompt you to speak commands prefixed with "ლუნა" (LUNA in Georgian). You can give voice commands to open or close applications, control music playback on Spotify, and perform other actions specified in the `commands.json` file.

`3.` To stop LUNA, simply say "გაჩერდი" or "ჩაქრი" and the script will terminate.
