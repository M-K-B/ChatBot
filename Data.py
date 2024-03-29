import pickle
import os
class User:
    def __init__(self, DisplayName, DiscordId, NumberOfRequests, Greeting):
        self.displayName = DisplayName
        self.discordId = DiscordId
        self.numberOfRequests = NumberOfRequests
        self.greeting = Greeting

    def setGreeting(self, string):
        """Search string to see if any of the commom greeting have been used"""
        if self.greeting == 'na':
            goodGreetings = ["good morning", "good afternoon", "good evening"]
            for word in goodGreetings:
                if word in string:
                    wordR = word.replace(" ", "-")
                    string.replace(word, wordR)
            #The reason the above for loop can't work all greetings is that the characters may be used as of another word. Most notability is towards "hi".
            lstGreetings = {"standard":["hi","hello","hey"],
            "posh":["greetings", "good-morning", "good-afternoon", "good-evening"], 
            "slang":["sound", "safe", "yo","howdy","wassup","sayin","wagw1"]}
            arrInp = str(string).split(" ")
            for word in arrInp:
                for key, val in lstGreetings.items():
                    for greet in val:
                        if word == greet:
                            if "-" in greet:
                                greet = greet.replace("-", " ")
                            self.greeting = greet
            #Going through each word within the string and comparing it to each word in the dictionary
    def numOfReqExceeded(self):
        if self.numberOfRequests > 10:
            return True
        else:
            return False

class Data:
    def __init__(self):
        self.content = self.__readFile()

    def __readFile(self):
        if os.path.exists("data.pkl"):
            with open("data.pkl", 'rb') as inFile:
                data = pickle.load(inFile)
        else:
            data = {}
        return data
    
    def readFile(self):
        self.content = self.__readFile("data.pkl")
    
    def writeFile(self):
        if os.path.exists("data.pkl"):
            os.remove("data.pkl")
        with open("data.pkl", 'wb') as outfile:
            pickle.dump(self.content, outfile, pickle.HIGHEST_PROTOCOL)

    def processUser(self, user):
        if user.discordId not in self.content:
            self.content[user.discordId] = user

if __name__ == "__main__":
    u1 = User("name", "4", 0, "na")
    u2 = User("name1", "5", 0, "na")
    data = Data()
    data.content[u1.discordId] = u1
    data.content[u2.discordId] = u2
    print(data.content)
    data.writeFile()