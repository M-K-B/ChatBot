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
        reqCount = 0
        for i in range(len(self.__entrySpit)):
            word = self.__entrySpit[i].lower()
            if 'help' == word:
                reqCount += 1
                if reqCount == 2:
                    return "Apologies, it looks like multiple requests have been made here."
                    break
                output = self.__HelpInfo()
                self.__data.content[self.user.discordId].numberOfRequests += 1
            if 'footballodds' == word:
                reqCount += 1
                if reqCount == 2:
                    return "Apologies, it looks like multiple requests have been made here."
                    break
                output = FootballOdds(self.__entrySpit[i+1].lower())
                if output != "Invalid input":
                    reqCount += 1
                self.__data.content[self.user.discordId].numberOfRequests += 1
            if 'playerpoints' == word:
                reqCount += 1
                if reqCount == 2:
                    return "Apologies, it looks like multiple requests have been made here."
                    break
                output = PlayerPoints(self.__entrySpit[i+1].lower())
                if output != "Invalid input":
                    reqCount += 1
                self.__data.content[self.user.discordId].numberOfRequests += 1
            if 'champleagues' == word:
                reqCount += 1
                if reqCount == 2:
                    return "Apologies, it looks like multiple requests have been made here."
                    break
                output = Cleagues(self.__entrySpit[i+1].lower())
                if output != "Invalid input":
                    reqCount += 1
                self.__data.content[self.user.discordId].numberOfRequests += 1
            if 'livescore' == word:
                reqCount += 1
                if reqCount == 2:
                    return "Apologies, it looks like multiple requests have been made here."
                    break
                output = livescore(self.__entrySpit[i+1].lower())
                if output != "Invalid input":
                    reqCount += 1
                self.__data.content[self.user.discordId].numberOfRequests += 1
            if 'teams' == word:
                reqCount += 1
                if reqCount == 2:
                    return "Apologies, it looks like multiple requests have been made here."
                    break
                output = jprint(self.__entrySpit[i+1].lower())
                if output != "Invalid input":
                    reqCount += 1
                self.__data.content[self.user.discordId].numberOfRequests += 1
            if 'player' == word:
                reqCount += 1
                if reqCount == 2:
                    return "Apologies, it looks like multiple requests have been made here."
                    break
                output = jprint(self.__entrySpit[i+1].lower())
                if output != "Invalid input":
                    reqCount += 1
                self.__data.content[self.user.discordId].numberOfRequests += 1
            if 'countries' == word:
                reqCount += 1
                if reqCount == 2:
                    return "Apologies, it looks like multiple requests have been made here."
                    break
                output = jprint(self.__entrySpit[i+1].lower())
                if output != "Invalid input":
                    reqCount += 1
                self.__data.content[self.user.discordId].numberOfRequests += 1
        if reqCount == 1:
            return output
        else:
            return "No valid request was made. Please try against or type help for request list."

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