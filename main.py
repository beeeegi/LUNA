import speech_recognition as sr
import spotipy.util as s_util
from AppOpener import open as open_app
from AppOpener import close as close_app
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import coloredlogs, logging, json, os, time, requests, spotipy

coloredlogs.install(level='INFO', fmt='%(levelname)s %(name)s %(message)s')
logger = logging.getLogger('LUNA')
logger.setLevel(logging.INFO)
load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SPOTIPY_USERNAME = os.getenv("SPOTIPY_USERNAME")
token = s_util.prompt_for_user_token(SPOTIPY_USERNAME, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope='user-modify-playback-state')
spotify_client = spotipy.Spotify(auth=token)


def recognize_speech():
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

def load_commands():
    with open("commands.json", "r", encoding="utf-8") as file:
        commands_data = json.load(file)
    return commands_data.get("commands", [])

def write(text):
    file_path = "test/natqvami.txt"
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + "\n")

def commands_to_discord(text):
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

commands = load_commands()
luna = "ლუნა"
commands_to_discord("✅ გული მიცემს ✅")

while True:
    spoken_text = recognize_speech()
    
    try:
        write(spoken_text)
    except TypeError as e:
        if "unsupported operand" in str(e):
            pass
        else:
            logger.warning(e)
    except Exception as e:
        logger.warning(e)

    if spoken_text:
        if luna in spoken_text:
            is_luna_active = True
            if is_luna_active:
                if "ჩართე" in spoken_text.lower():
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                open_app(command["application"], match_closest=True, output=False)

                                logger.info(f"vxsni aplikacias - {app}")
                                commands_to_discord(f"ვხსნი აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
                elif "გახსენი" in spoken_text.lower():
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                open_app(command["application"], match_closest=True, output=False)
    
                                logger.info(f"vxsni aplikacias - {app}")
                                commands_to_discord(f"ვხსნი აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
    
    
                elif "გამორთე" in spoken_text.lower():
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                close_app(command["application"], match_closest=True, output=False)
    
                                logger.info(f"vtishav aplikacias - {app}")
                                commands_to_discord(f"ვხურავ აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
                elif "გათიშე" in spoken_text.lower():
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                close_app(command["application"], match_closest=True, output=False)
    
                                logger.info(f"vtishav aplikacias - {app}")
                                commands_to_discord(f"ვხურავ აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
                elif "დახურე" in spoken_text.lower():
                    for command in commands:
                        if command["trigger"] in spoken_text:
                            try:
                                app = command["application"]
                                close_app(command["application"], match_closest=True, output=False)
    
                                logger.info(f"vtishav aplikacias - {app}")
                                commands_to_discord(f"ვხურავ აპლიკაციას - {app}")
                            except Exception as e:
                                logger.warning(e)
    
    
                elif "გადართე მუსიკა" in spoken_text.lower():
                    try:
                        spotify_client.next_track(device_id=None)
                        commands_to_discord("⏭️ გადავრთე მუსიკა")
                        logger.info("musika gadavrte")
                    except Exception as e:
                        logger.warning(e)
                elif "გააგრძელე მუსიკა" in spoken_text.lower():
                    try:
                        spotify_client.start_playback(device_id=None)
                        commands_to_discord("▶️ გავაგრძელე მუსიკა")
                        logger.info("musika gavagrdzele")
                    except Exception as e:
                        logger.warning(e)
                elif "დააპაუზე მუსიკა" in spoken_text.lower():
                    try:
                        spotify_client.pause_playback(device_id=None)
                        commands_to_discord("⏸️ დავაპაუზე მუსიკა")
                        logger.info("musika davapauze")
                    except Exception as e:
                        logger.warning(e)
                    
    
    
                elif "გაჩერდი" in spoken_text.lower():
                    logger.critical("shevwyvite mushaoba")
                    commands_to_discord("❌ გული აღარ მიცემს ❌")
                    exit()
                elif "ჩაქრი" in spoken_text.lower():
                    logger.critical("shevwyvite mushaoba")
                    commands_to_discord("❌ გული აღარ მიცემს ❌")
                    exit()
    
    
                elif "ჩააქრე კომპიუტერი" in spoken_text.lower():
                    logger.critical("KOMPIUTERI GAITISHEBA 5 WAMSHI")
                    time.sleep(1)
                    logger.critical("KOMPIUTERI GAITISHEBA 4 WAMSHI")
                    time.sleep(1)
                    logger.critical("KOMPIUTERI GAITISHEBA 3 WAMSHI")
                    time.sleep(1)
                    logger.critical("KOMPIUTERI GAITISHEBA 2 WAMSHI")
                    time.sleep(1)
                    logger.critical("KOMPIUTERI GAITISHEBA 1 WAMSHI")
                    time.sleep(1)
                    logger.critical("VTISHAV KOMPIUTERS")
                    commands_to_discord("❌ მომხმარებელმა გათიშა კომპიუტერი ❌")
                    
                    time.sleep(1)
                    os.system("shutdown /s")
                else:
                    logger.warning("brdzaneba ver davafiqsire")

                is_luna_active = False
            else:
                logger.warning("ar var aqtiuri")
        else:
            logger.info("velodebi chems saxels")
    else:
        logger.warning("velodebi brdzanebas")