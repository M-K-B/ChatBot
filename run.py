from Data import *
from FootballOdds import *
from livescores import *
from leagues import *
from fantasyStats import *
from teams import *
from players import *
from countries import *
import string

class functions:
    def __init__(self, User, Entry):
        self.user = User
        self.entry = Entry
        self.__data = Data()
        self.__entrySpit = Entry.split(" ")

    def __textSend(self):
        """runs through the text send by the user to analyse which function should be ran"""
        self.__data.content[self.user.discordId].setGreeting(self.entry)
        reqCount = 0
        if not self.__data.content[self.user.discordId].numOfReqExceeded():
            for i in range(len(self.__entrySpit)):
                word = self.__entrySpit[i].lower()
                if 'help' == word:
                    if reqCount == 2:
                        return self.__greet() + "Apologies, it looks like multiple requests have been made here."
                        break
                    output = self.__HelpInfo()
                    if output != "Invalid input":
                        reqCount += 1
                    self.__data.content[self.user.discordId].numberOfRequests += 1
                if 'footballodds' == word:
                    if reqCount == 2:
                        return self.__greet() + "Apologies, it looks like multiple requests have been made here."
                        break
                    output = FootballOdds(self.__entrySpit[i+1].lower())
                    if output != "Invalid input":
                        reqCount += 1
                    self.__data.content[self.user.discordId].numberOfRequests += 1
                if 'playerpoints' == word:
                    if reqCount == 2:
                        return self.__greet() + "Apologies, it looks like multiple requests have been made here."
                        break
                    output = PlayerPoints(self.__entrySpit[i+1].lower())
                    if output != "Invalid input":
                        reqCount += 1
                    self.__data.content[self.user.discordId].numberOfRequests += 1
                if 'champleagues' == word:
                    if reqCount == 2:
                        return self.__greet() + "Apologies, it looks like multiple requests have been made here."
                        break
                    output = Cleagues(self.__entrySpit[i+1].lower())
                    if output != "Invalid input":
                        reqCount += 1
                    self.__data.content[self.user.discordId].numberOfRequests += 1
                if 'livescore' == word:
                    if reqCount == 2:
                        return self.__greet() + "Apologies, it looks like multiple requests have been made here."
                        break
                    output = livescore(self.__entrySpit[i+1].lower())
                    if output != "Invalid input":
                        reqCount += 1
                    self.__data.content[self.user.discordId].numberOfRequests += 1
                if 'teams' == word:
                    if reqCount == 2:
                        return self.__greet() + "Apologies, it looks like multiple requests have been made here."
                        break
                    output = jprint(self.__entrySpit[i+1].lower())
                    if output != "Invalid input":
                        reqCount += 1
                    self.__data.content[self.user.discordId].numberOfRequests += 1
                if 'player' == word:
                    if reqCount == 2:
                        return self.__greet() + "Apologies, it looks like multiple requests have been made here."
                        break
                    output = play45(self.__entrySpit[i+1].lower())
                    if output != "Invalid input":
                        reqCount += 1
                    self.__data.content[self.user.discordId].numberOfRequests += 1
                if 'countries' == word:
                    if reqCount == 2:
                        return self.__greet() + "Apologies, it looks like multiple requests have been made here."
                        break
                    output = coun(self.__entrySpit[i+1].lower())
                    if output != "Invalid input":
                        reqCount += 1
                    self.__data.content[self.user.discordId].numberOfRequests += 1
            self.__data.writeFile()
            if reqCount == 1:
                return self.__greet() + output
            else:
                return self.__greet() + "No valid request were made. Please try again or type help for request list."
        else:
            return self.__greet() + "You have hit the limit for the number of requests that can be made. Please contact 0121 123 1234 to purchase additional requests."

    def __greet(self):
        if self.__data.content[self.user.discordId].greeting == "na":
            return f"Hi {self.__data.content[self.user.discordId].displayName},\n\n"
        return f"{self.__data.content[self.user.discordId].greeting[0].upper()}{self.__data.content[self.user.discordId].greeting[1:len(self.__data.content[self.user.discordId].greeting)]} {self.__data.content[self.user.discordId].displayName},\n\n"

    def __HelpInfo(self):
        """Creates the help string if the user requests for help"""
        dit = {"FootballOdds":"Obtain the odds on an upcoming game for a given team",
            "Teams":"Print team information",
            "ChampLeagues":"Print championship leagues information",
            "Player":"Print player information",
            "Countries":"Print countries going into the euros",
            "Livescore":"Live score of the league you put in",
            "PlayerPoints":"Obtain a players fantasy points and relevant information this season"}
        #All function options and usage
        output = "Input one of the following functions and lead the function with a request parameter based on the function:\n"
        for key, value in dit.items():
            pass
            if len(key) < 8:
                output += f"{key}:\t{value}\n"
            elif len(key) < 16:
                output += f"{key}:\t{value}\n"
            elif len(key) < 24:
                output += f"{key}:\t{value}\n"
        return output

    def run(self):
        """User has made a request which means adding them to the data file and returning a string back to discord"""
        self.__data.processUser(self.user)
        return self.__textSend()

if __name__ == "__main__":
    
    print(livescore("Prem"))