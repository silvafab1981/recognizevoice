import pyttsx3

def say(engine, text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def set_tts():
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1.0)
    #agregar un for each recorrer las voces listarlas
    # y permitir elegir una de ellas
    voices = engine.getProperty('voices')
    
    print("Seleccione una voz:")
    for i, voice in enumerate(voices):
        print(f"{i+1}. {voice.name}")
    choice = input("Opción: ")
    engine.setProperty('voice', voices[int(choice)-1].id)
        
    engine.setProperty('voice', voices[3].id)
    return engine