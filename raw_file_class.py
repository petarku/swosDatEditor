
class RawPlayerData:
    playerName = bytes(22)
    playerShirtNo = bytes(1) 
class RawClubData:
    name  = bytes(12)
    division = bytes(1) 
    coach = bytes(22) 
    rawPlayerData = []

    def add_players(self):
        self.rawPlayerData.append(RawPlayerData())

class RawDatFile:
    rawClubData = [] 
    numberOfTeams = bytes(2) 
    def add_club_data(self,RawClubData):
        self.rawClubData.append(RawClubData)





      
   
    