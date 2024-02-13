import speech_recognition as sr
import spotipy.util as s_util
from AppOpener import open as open_app
from AppOpener import close as close_app
from dotenv import load_dotenv
import spotipy.oauth2 as oauth2
import coloredlogs, logging, json, os, time, requests, spotipy

# logging and dotenv setup
coloredlogs.install(level='INFO', fmt='%(levelname)s %(name)s %(message)s')
logger = logging.getLogger('LUNA')
logger.setLevel(logging.INFO)
load_dotenv()

# spotify setup
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SPOTIPY_USERNAME = os.getenv("SPOTIPY_USERNAME")
token = s_util.prompt_for_user_token(
    SPOTIPY_USERNAME,
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope='user-modify-playback-state'
)
sp_oauth = oauth2.SpotifyOAuth(
    SPOTIPY_CLIENT_ID,
    SPOTIPY_CLIENT_SECRET,
    SPOTIPY_REDIRECT_URI,
    scope='user-modify-playback-state',
    cache_path=".cache",
)
spotify_client = spotipy.Spotify(auth=token)

# refresh spotify token if expired
def refreshTokenIfExpired():
    token_info = sp_oauth.get_access_token()

    if token_info and sp_oauth.is_token_expired(token_info):
        new_token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        new_token = new_token_info['access_token']
        return new_token
    elif token_info:
        return token_info['access_token']
    else:
        return None

# function to recognize speech input
def recognizeSpeech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        logger.info("gismen...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="ka-GE")
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        logger.warning(e)
        return None

# load commands from JSON file
def loadCommands():
    with open("commands.json", "r", encoding="utf-8") as file:
        commands_data = json.load(file)
    return commands_data.get("commands", [])

# write speech input to file
def writeToFile(text):
    file_path = os.getenv("SPEECH_FILE_PATH")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + "\n")

# send executed commands to discord
def commandsToDiscord(text):
    webhook = os.getenv("DISCORD_WEBHOOK_URL")

    prefix = """```ansi
[2;30m[2;34m[[0m[2;30m[0m[2;34m[1;34mLUNA][0m[1;34m [1;37m->[0m[1;34m[1;36m[0m[1;34m[0m[2;34m[0m """
    suffix = """```"""
    msg = prefix + text + suffix

    payload = {
        "content": msg
    }

    response = requests.post(webhook, json = payload)
    if response == 204:
        logger.info("gavagzavne natqvami discordshi")

# load commands and initialize variables
commands = loadCommands()
luna = "ლუნა"
commandsToDiscord("✅ გული მიცემს ✅")

while True:
    spoken_text = recognizeSpeech()
    
    # write speech input to file
    try:
        writeToFile(spoken_text)
    except TypeError as e:
        if "unsupported operand" in str(e):
            pass
        else:
            logger.warning(e)
    except Exception as e:
        logger.warning(e)

    # checks if spoken_text exists
    if spoken_text:
        # checks if "ლუნა" exists in variable `spoken_text`
        if luna in spoken_text:
            # makes luna active
            is_luna_active = True
            if is_luna_active:
                # checks if "ჩართე"(open) is in spoken_text variable
                if "ჩართე" in spoken_text.lower():
                    # loops trough all of the commands and checks if the trigger word is found in `spoken_text`
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                open_app(command["application"], match_closest=True, output=False)

                                logger.info(f"vxsni aplikacias - {app}")
                                commandsToDiscord(f"ვხსნი აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
                # checks if "გახსენი"(open) is in spoken_text variable
                elif "გახსენი" in spoken_text.lower():
                    # loops trough all of the commands and checks if the trigger word is found in `spoken_text`
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                open_app(command["application"], match_closest=True, output=False)
    
                                logger.info(f"vxsni aplikacias - {app}")
                                commandsToDiscord(f"ვხსნი აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
    
                # checks if "გამორთე"(close) is in spoken_text variable
                elif "გამორთე" in spoken_text.lower():
                    # loops trough all of the commands and checks if the trigger word is found in `spoken_text`
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                close_app(command["application"], match_closest=True, output=False)
    
                                logger.info(f"vtishav aplikacias - {app}")
                                commandsToDiscord(f"ვხურავ აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
                # checks if "გათიშე"(close) is in spoken_text variable
                elif "გათიშე" in spoken_text.lower():
                    # loops trough all of the commands and checks if the trigger word is found in `spoken_text`
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                close_app(command["application"], match_closest=True, output=False)
    
                                logger.info(f"vtishav aplikacias - {app}")
                                commandsToDiscord(f"ვხურავ აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
                # checks if "დახურე"(close) is in spoken_text variable
                elif "დახურე" in spoken_text.lower():
                    # loops trough all of the commands and checks if the trigger word is found in `spoken_text`
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                close_app(command["application"], match_closest=True, output=False)
    
                                logger.info(f"vtishav aplikacias - {app}")
                                commandsToDiscord(f"ვხურავ აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
    
                # checks if "გადართე მუსიკა"(next track) is in spoken_text variable
                elif "გადართე მუსიკა" in spoken_text.lower():
                    token = refreshTokenIfExpired()
                    spotify_client = spotipy.Spotify(auth=token)

                    spotify_client.next_track(device_id=None)
                    commandsToDiscord("⏭️ გადავრთე მუსიკა")
                    logger.info("musika gadavrte")
                # checks if "გააგრძელე მუსიკა"(continue playback) is in spoken_text variable
                elif "გააგრძელე მუსიკა" in spoken_text.lower():
                    try:
                        token = refreshTokenIfExpired()
                        spotify_client = spotipy.Spotify(auth=token)
                        
                        spotify_client.start_playback(device_id=None)
                        commandsToDiscord("▶️ გავაგრძელე მუსიკა")
                        logger.info("musika gavagrdzele")
                    except Exception as e:
                        logger.warning(e)
                # checks if "დააპაუზე მუსიკა"(pause playback) is in spoken_text variable
                elif "დააპაუზე მუსიკა" in spoken_text.lower():
                    try:
                        token = refreshTokenIfExpired()
                        spotify_client = spotipy.Spotify(auth=token)
                        
                        spotify_client.pause_playback(device_id=None)
                        commandsToDiscord("⏸️ დავაპაუზე მუსიკა")
                        logger.info("musika davapauze")
                    except Exception as e:
                        logger.warning(e)
                    
                # checks if "გაჩერდი"(stop) is in spoken_text variable
                elif "გაჩერდი" in spoken_text.lower():
                    logger.critical("shevwyvite mushaoba")
                    commandsToDiscord("❌ გული აღარ მიცემს ❌")
                    exit()
                # checks if "ჩაქრი"(stop) is in spoken_text variable
                elif "ჩაქრი" in spoken_text.lower():
                    logger.critical("shevwyvite mushaoba")
                    commandsToDiscord("❌ გული აღარ მიცემს ❌")
                    exit()
    
    
                # checks if "ჩააქრე კომპიუტერი"(shutdown the computer) is in spoken_text variable
                elif "ჩააქრე კომპიუტერი" in spoken_text.lower():
                    z = 5
                    for i in range(z):
                        logger.critical(f"KOMPIUTERI GAITISHEBA {z} WAMSHI")
                        z -= 1
                        time.sleep(1)

                    logger.critical("VTISHAV KOMPIUTERS")
                    commandsToDiscord("❌ მომხმარებელმა გათიშა კომპიუტერი ❌")
                    time.sleep(1)
                    os.system("shutdown /s")

                # makes luna inactive
                is_luna_active = False
            else:
                logger.warning("ar var aqtiuri")
        else:
            logger.info("velodebi chems saxels")
    else:
        logger.warning("velodebi brdzanebas")