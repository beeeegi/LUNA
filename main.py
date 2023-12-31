import speech_recognition as sr
from AppOpener import open as open_app
from AppOpener import close as close_app
from dotenv import load_dotenv
import coloredlogs, logging, json, os, time, requests

coloredlogs.install(level='DEBUG', fmt='%(levelname)s %(name)s %(message)s')

logger = logging.getLogger('LUNA')
logger.setLevel(logging.DEBUG)
load_dotenv()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        logger.info("gismen...")
        audio = recognizer.listen(source, timeout=30)
    try:
        text = recognizer.recognize_google(audio, language="ka-GE")
        return text
    except sr.UnknownValueError:
        logger.warning("ver gavige ra mitxari...")
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
    else:
        logger.warning(response)

commands = load_commands()

is_luna_active = False      # gatishvaze cmd ar gaitishos, aramed smena shewyvitos  
luna_trigger = "ლუნა"

commands_to_discord("✅ გული მიცემს ✅")
while True:
    spoken_text = recognize_speech()
    
    try:
        write(spoken_text)
    except Exception as e:
        logger.warning(e)

    if spoken_text:
        if luna_trigger in spoken_text:
            if "ჩართე" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            app = command["application"]
                            open_app(command["application"], match_closest=True, output=False)

                            logger.debug(f"vxsni aplikacias - {app}")
                            commands_to_discord(f"ვხსნი აპლიკაციას - {app}")
                        except Exception as e:
                            logger.warning(e)
            elif "გახსენი" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            app = command["application"]
                            open_app(command["application"], match_closest=True, output=False)

                            logger.debug(f"vxsni aplikacias - {app}")
                            commands_to_discord(f"ვხსნი აპლიკაციას - {app}")
                        except Exception as e:
                            logger.warning(e)


            elif "გამორთე" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            app = command["application"]
                            close_app(command["application"], match_closest=True, output=False)

                            logger.error(f"vtishav aplikacias - {app}")
                            commands_to_discord(f"ვხურავ აპლიკაციას - {app}")
                        except Exception as e:
                            logger.warning(e)
            elif "გათიშე" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            app = command["application"]
                            close_app(command["application"], match_closest=True, output=False)

                            logger.error(f"vtishav aplikacias - {app}")
                            commands_to_discord(f"ვხურავ აპლიკაციას - {app}")
                        except Exception as e:
                            logger.warning(e)
            elif "დახურე" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            app = command["application"]
                            close_app(command["application"], match_closest=True, output=False)

                            logger.error(f"vtishav aplikacias - {app}")
                            commands_to_discord(f"ვხურავ აპლიკაციას - {app}")
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
                logger.warning("warmoishva amoucnobi shecdoma, daukavshirdit mflobels")
        else:
            logger.info("velodebi chems saxels")
    else:
        logger.warning("warmoishva amoucnobi shecdoma, daukavshirdit mflobels")