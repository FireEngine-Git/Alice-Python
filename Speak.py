import pyttsx3

class Speak:
    def __init__(self):
        self.speed = 180
        self.engine = pyttsx3.Engine()
        self.engine.setProperty("rate", self.speed)

    def Speak(self, query):
        self.engine.say(query)
        self.engine.runAndWait()
    
if __name__ == "__main__":
    speaker = Speak()
    print("staring to speak")
    speaker.Speak("Hello 1 2 3 mic check how are you doing")
    print("DONE")
