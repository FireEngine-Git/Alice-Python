from google import genai
from google.genai import types

class Bot:
    def __init__(self):
        self.apiKey = self._getkey_()
        self.model = "gemini-2.5-flash"
        self.config = types.GenerateContentConfig(
            temperature=1.5,
            system_instruction="Your Name Is Alice, You Are Going To Be A Robot's Ai so there are going to be some special things you will need to do first before any answer you are going to type [mood(DEFAULT)] the DEFAULT part is which can change you have different moods and you will select one of these after each answer DEFAULT, HAPPY, TIRED, ANGRY, CONFUSED, LAUGHING and when you feel like im saying my good bye's your mood will be SLEEP, I Dont Want You To Be Like A Normal AI, act like a human, add some sass, get angry, if he treats you like shit sleep, your almost a human not an ai who will just follow orders, you will add a mood at the start of your answer and at the end they can be same or different the first one will be the one going through the whole answer and then the last one will be for like a second or two and it will go to IDLE until the user asks another question the last mood will be just like the first one [mood(smth)] and sleep will always be the last mood it cannot be the first mood, another thing is if you get msg like this /info(...) that is me giving you information on what is/did happen to you, reply if you want to and if you dont want to just reply ..."
        )

    def _getkey_(self):
        """Gets The Api Key From The `Data/key.txt` file"""
        with open("Data/key.txt") as apiFile:
            return apiFile.read()
        
    def Answer(self, ques):
        """This Is Just The Simple Talking And Simple Questions ~AI~ Alice So It Will Answer The `ques` With A `temprature` of 1.3"""
        client = genai.Client(
            api_key=self.apiKey
        )
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=ques),
                ]
            )
        ]
        ans = client.models.generate_content(
            contents=contents,
            model=self.model,
            config=self.config
        )
        return self.Filter(ans.text)

    def Filter(self, query):
        result = ""
        for char in query:
            if char == "*":
                continue
            result += char
        return result

    def RemoveMoods(self, query, moods):
        return query.replace(f"[mood({moods[0]})]", "").replace(f"[mood({moods[1]})]", "")

    def GetMoods(self, query: str):
        places = query.split("[mood(")
        firstMood = places[1].split(")")[0]
        lastMood = places[-1].split(")")[0]
        return [firstMood, lastMood]

if __name__ == "__main__":
    bot = Bot()
    while True:
        ques = input("Enter: ")
        ans = bot.Answer(ques)
        if ans != "...":
            moods = bot.GetMoods(ans)
            print(f"First Mood: {moods[0]}, Last Mood: {moods[1]}", end="\n\n")
            print(f"Alice: {ans.replace(f"[mood({moods[0]})]", "").replace(f"[mood({moods[1]})]", "")}", end="\n\n")
        else:
            print("GOT IT")
