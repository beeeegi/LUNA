import speech_recognition as sr
from AppOpener import open

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("gismen...")
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio, language="ka-GE")
        return text
    except sr.UnknownValueError:
        print("ver gavige...")
        return None
    except sr.RequestError as e:
        print(f"google speech recognition service error: {e}")
        return None

while True:
    text = recognize_speech()
    spoken_text = text.lower()

    if spoken_text:
        if "შეწყვეტა" in spoken_text:
            print("jarvisma shewyvita mushaoba")
            break
        if "გახსენი ოპერა" in spoken_text:
            try:
                open("OperaGX", match_closest=True)
                print("++ gaixsna opera")
            except Exception as e:
                print(f"racxa errori: {e}")
        elif "გახსენი ლოლი" in spoken_text:
            try:
                open("LeagueOfLegends", match_closest=True)
                print("++ gaixsna loli")
            except Exception as e:
                print(f"racxa errori: {e}")
        else:
            print("tqveni brdzaneba araa agbechdili")

            
            
    


