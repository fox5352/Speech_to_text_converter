import speech_recognition as sr


class Converter:
    audio_list = []
    transcript = []

    def __int__(self):
        self.recognizer = sr.Recognizer

    @staticmethod
    def lister() -> object:
        with sr.Microphone() as source:
            audio = sr.Recognizer().listen(source)
            return audio

    @staticmethod
    def converter(audio: object) -> str:
        text = ""

        try:
            # Recognize the speech
            text = sr.Recognizer().recognize_google(audio_data=audio)
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

        return text
