import speech_recognition as sr
from AppOpener import open as open_app
from AppOpener import close as close_app
import json

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("gismen...")
        audio = recognizer.listen(source, timeout=60)

    try:
        text = recognizer.recognize_google(audio, language="ka-GE")
        return text
    except sr.UnknownValueError:
        print("ver gavige...")
        return None
    except sr.RequestError as e:
        print(f"google speech recognition service error: {e}")
        return None

def load_commands():
    with open("commands.json", "r", encoding="utf-8") as file:
        commands_data = json.load(file)
    return commands_data.get("commands", [])

def write(text):
    file_path = "test/natqvami.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

commands = load_commands()

is_jarvis_active = False
jarvis_trigger = "ყლეო"


while True:
    spoken_text = recognize_speech()
    
    try:
        write(spoken_text)
    except Exception as e:
        print(f"racxa errori: {e}")

    if spoken_text:
        if jarvis_trigger in spoken_text:
            is_jarvis_active = True


            if "ჩართე" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            open_app(command["application"], match_closest=True)
                        except Exception as e:
                            print(f"racxa errori: {e}")
            elif "გახსენი" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            open_app(command["application"], match_closest=True)
                        except Exception as e:
                            print(f"racxa errori: {e}")


            elif "გამორთე" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            close_app(command["application"], match_closest=True)
                        except Exception as e:
                            print(f"racxa errori: {e}")
            elif "გათიშე" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            close_app(command["application"], match_closest=True)
                        except Exception as e:
                            print(f"racxa errori: {e}")
            elif "დახურე" in spoken_text.lower():
                for command in commands:
                    if command["trigger"] in spoken_text:
                        try:
                            close_app(command["application"], match_closest=True)
                        except Exception as e:
                            print(f"racxa errori: {e}")


            elif "გაჩერდი" in spoken_text.lower():
                print("jarvisma shewyvita mushaoba")
                exit()
            elif "ჩაიჯვი" in spoken_text.lower():
                print("jarvisma shewyvita mushaoba")
                exit()
            else:
                print("GAVIGE ISETI OPERATORI ROMELIC AR MISWAVLIA")
        else:
            is_jarvis_active = False
    else:
        print("warmoishva amoucnobi shecdoma")














