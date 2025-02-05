# Luna | PENDING RE-WRITE
J.A.R.V.I.S ripoff but in Georgian Language.

J.A.R.V.I.S. is a fictional character voiced by Paul Bettany in the Marvel Cinematic Universe film franchise, based on the Marvel Comics characters Edwin Jarvis and H.O.M.E.R., respectively the household butler of the Stark family and another AI designed by Stark.

## Usage
### Installing Dependencies
`-` Run the following command to install the required dependencies
```
pip install -r requirements.txt
```
### Setting Up Environment Variables
`1.` Create a file named .env in the same directory as your script.

`2.` Inside the .env file, define the following environment variables:
```env
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=your_spotify_redirect_uri
SPOTIPY_USERNAME=your_spotify_username
DISCORD_WEBHOOK_URL=your_discord_webhook_url
SPEECH_FILE_PATH=your_path
```
### Running and using LUNA
`1.` Run the following command in your terminal or command prompt
```
python main.py
```
`2.` LUNA will prompt you to speak commands prefixed with "ლუნა" (LUNA in Georgian). You can give voice commands to open or close applications, control music playback on Spotify, and perform other actions specified in the `commands.json` file.

`3.` To stop LUNA, simply say "გაჩერდი" or "ჩაქრი" and the script will terminate.
### Writing Speech Input to File
The `writeToFile()` function is responsible for saving the recognized speech input to a text file.
```py
def writeToFile(text):
    file_path = os.getenv("SPEECH_FILE_PATH")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + "\n")
```
Don't forget to change `your_path` in `.env` file to your own path.
