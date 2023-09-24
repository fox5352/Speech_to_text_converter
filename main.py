import speech_recognition as sr

from Audio_converter import Converter

def file_listener(recognizer, path):
    with sr.AudioFile(path) as source:
        print("file listener started")
        audio = recognizer.listen(source)
        return audio

def converter(recognizer,audio):
    print("processing ...")
    text = ''
    try:
        # Recognize the speech
        text = recognizer.recognize_google(audio)  # You can use other APIs like recognize_sphinx or recognize_bing
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    print("procesing complete")
    print()
    return text

def file_writer(file_name, transcript):
    with open(f'{file_name}.txt', "a") as file:
        for line in transcript:
            file.write(f'{line}\n')

    print(f'{file_name}.txt successfully created')   
    

def main():
    transcript = []
    stt = Converter()
    said_exit = False    

    while not said_exit:
        print("listening...")
        audio = stt.lister()
        print("processing...")
        text = stt.converter(audio=audio)

        transcript.append(text)
        
        print(f'you said :{text}')
        print()
        
        if text == "exit":
            said_exit = True

    create_file = input("would you like to save transcript to a file? Y/N   :")
    
    print(create_file)

    if create_file == "y" or create_file == "Y" :
        file_name = input("file_name? :")
        file_writer(file_name, transcript[0:-2])
    print("program ended")


if __name__ == "__main__":
    main()
