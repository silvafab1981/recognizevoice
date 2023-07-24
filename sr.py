import speech_recognition as sr
import tts

if __name__ == "__main__":
    engine = tts.set_tts()
    r = sr.Recognizer()


with sr.Microphone() as source:
    tts.say(engine, "Hola Fabi, decime algo")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print("Reconociendo...")
    #Permitir elegir de los lenguajes"
    try:
        text = r.recognize_google(audio, language="es-MX")
        print("Dijiste: {}".format(text))
        tts.say(engine, "Dijiste: " + text)
    except:
        print("No te escuche")