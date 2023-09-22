import speech_recognition as sr


def mic_listener(recognizer):
    with sr.Microphone() as source:
        print("Mic is open to talk")
        audio = recognizer.listen(source)
        print("audio captured")
        return audio

def file_listener(recognizer, path):
    with sr.AudioFile(path) as source:
        print("file listener started")
        audio = recognizer.listen(source)
        return audio

def converter(recognizer,audio):
    print("processing ...")
    try:
        # Recognize the speech
        text = recognizer.recognize_google(audio)  # You can use other APIs like recognize_sphinx or recognize_bing
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    print("procesing complete")
    return text

def main():
    transcript = []
    recognizer  = sr.Recognizer()
    
    said_exit = False    

    while not said_exit:
        audio = mic_listener(recognizer)
        text = converter(recognizer, audio)
        
        transcript.append(text)
        
        print(f'you said :{text}')
        
        if text == "exit":
            said_exit = True
        
   
    print("program ended")


if __name__ == "__main__":
    main()