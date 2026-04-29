from ChatBot import Bot
from Speak import Speak
from Comms import Comms

class AI:
    def __init__(self):
        self.bot = Bot()
        self.speaker = Speak()
        self.comms = Comms("COM22")

    def Run(self):
        while True:
            ques = input("Enter: ")
            ans = self.bot.Answer(ques)
            if ans != "...":
                moods = self.bot.GetMoods(ans)
                ans = self.bot.RemoveMoods(ans, moods)
                print(moods, end="\n\n")
                print(f"Alice: {ans.replace(f"[mood({moods[0]})]", "").replace(f"[mood({moods[1]})]", "")}", end="\n\n")
                self.comms.SendData(self.GetMoodCode(moods[0]))
                self.speaker.Speak(ans)
                self.comms.SendData(self.GetMoodCode(moods[1]))
            else:
                print("GOT IT")

    def GetMoodCode(self, mood):
        moodCodes = ["DEFAULT", "TIRED", "ANGRY", "HAPPY", "LAUGHING", "CONFUSED", "SLEEP"]
        return moodCodes.index(mood)

if __name__ == "__main__":
    ai = AI()
    ai.Run()
