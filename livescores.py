import requests
from bs4 import BeautifulSoup #import BeatifulSoup library used get the data from a website 
from datetime import date


def getTeams(teamlist):
    #checking from which league does teamlist belongs to
    if teamlist=='prem': #if teamlist belongs to Premier League
        premteamslist = ['Arsenal','AFC Bournemouth','Aston Villa','Brighton & Hove Albion','Burnley','Chelsea','Crystal Palace','Everton','Leicester City','Liverpool','Manchester City','Manchester United','Newcastle United','Norwich City','Sheffield United','Southampton','Tottenham Hotspur','Watford','West Ham United','Wolverhampton Wanderers']
    elif teamlist=='seriea': #if teamlist belongs to Serie A
        premteamslist=['Roma','Napoli','Juventus','Bologna','Inter Milan','Torino','Atalanta','Cagliari','Genoa','Udinese','Lecce','Sassuolo','Hellas Verona','Brescia','Fiorentina','Parma','AC Milan','Lazio']
    else: #if teamlist contains teams from different leagues       
        premteamslist = teamlist
    return premteamslist

def livescore(teamlist):
    datetoday = date.today() 
    #using BBC livescores website to get the data    
    url = 'https://www.bbc.co.uk/sport/football/scores-fixtures/'+str(datetoday) #using today's date to get livescores
    result = requests.get(url) #store extracted data in result
    #store the page HMTL with BeautifulSoup
    soup = BeautifulSoup(result.content, "html") 
    #look for all of the spans with the attribute class defined by the tag the home 
    #gets all of the teams name
    teams = soup.find_all("span",attrs={'class':"gs-u-display-none gs-u-display-block@m qa-full-team-name sp-c-fixture__team-name-trunc"}) 
    
    #storing data in four different lists because they all have different class names     
    #storing finished homes scores
    finishedhomescores = soup.find_all("span",attrs={'class':"sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--ft"})
    #storing livescores of home team
    livehomescores = soup.find_all("span",attrs={'class':"sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--live"})
    #storing finished games scores
    finishedawayscores = soup.find_all("span",attrs={'class':"sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--ft"})
    #storing livescore of away team
    liveawayscores = soup.find_all("span",attrs={'class':"sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--live"})
    #storing matchstatus such as Full time, Half time or live
    matchstatus = soup.find_all("span",attrs={'class':"sp-c-fixture__status-wrapper"})
    
    homenames = [] 
    awaynames = []
    homescores = []
    awayscores = []
    #checking which league to get the data from user input
    premteamslist=getTeams(teamlist)
    
    #stores the score of all the home teams
    premhomescores = []
    #stores the score of all the away teams
    premawayscores = []
    #store the time of each match or if it's Full time or Half time
    matchtimes = []
    premmatchtimes = []
    #counter for finished matches
    finishediterator = 0
    #counter for live matches
    liveiterator=0
    
    for j in range(0,len(matchstatus)):
        #if Full time append get result
        if(matchstatus[j].text=='FT'):      
            #append the score of home team to homescores list   
            homescores.append(finishedhomescores[finishediterator].text)
            #append the score of away team to  awayscores list 
            awayscores.append(finishedawayscores[finishediterator].text)
            #append the status of the match FT
            matchtimes.append(matchstatus[j].text)
            finishediterator+=1 #increase finished iterator so it only goes up when a finished match is appended
        #if matchstatus contains mins or + it means the match is live
        #if it contains HT it means it's Half time        
        elif(('mins' in matchstatus[j].text) or (matchstatus[j].text=='HT') or ('+' in matchstatus[j].text)):
            homescores.append(livehomescores[liveiterator].text)    
            awayscores.append(liveawayscores[liveiterator].text)
            matchtimes.append(matchstatus[j].text)
            liveiterator+=1 # counts the live matches
        else: #if match is being postponed or hasn't started
            homescores.append('N/A') 
            awayscores.append('N/A')
            matchtimes.append('N/A') 
    #premflag is a list of match status, I use to determine which match i need to get 
    premflag = [0]*len(matchstatus) 
    #for loop that goes through the list of teams by 2 steps, because it gets home team and away team
    for i in range(0,len(teams),2):  
        if(i>0):
            #updtating j because it only counts the matches, if j>0 it means that i 
            j=int(i/2)
        else:
            #this is to update j the first time iterating throught the team list
            j=0
        #check if in teamsList
        for k in range(0,len(premteamslist)): 
            if(teams[i].text==premteamslist[k]):                
                homenames.append(teams[i].text)
                awaynames.append(teams[i+1].text)
                premmatchtimes.append(matchtimes[j])            
                premflag[j]=1  
                break                  
    #get the scores
    for i in range(0,len(homescores)):
        if(premflag[i]==1): #if it's the match I need
            #append home and aways scores to their lists
            premhomescores.append(homescores[i])         
            premawayscores.append(awayscores[i])
    
    gamestrings = [] 
    for i in range(0,len(homenames)): 
        #creates a list of string with all the information needed for the match
        gamestrings.append(homenames[i]+' '+premhomescores[i] + ' - ' + premawayscores[i] + ' ' + awaynames[i]+' '+premmatchtimes[i])
  
    return gamestrings


if __name__ == "__main__":
    
    print(livescore("Prem"))