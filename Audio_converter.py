import speech_recognition as sr


class Converter:
    audio_list = []
    transcript = []

    def __int__(self):
        self.recognizer = sr.Recognizer

    @staticmethod
    def listener() -> object:
        with sr.Microphone() as source:
            audio = sr.Recognizer().listen(source)
            return audio

    @staticmethod
    def converter(audio: object, pipe) -> None:
        text = ""

        try:
            # Recognize the speech
            text = sr.Recognizer().recognize_google(audio_data=audio)
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

        pipe.send(text)
