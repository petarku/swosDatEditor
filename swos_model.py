from raw_file_class import RawClubData as rawClub 
class Club:
    def __init__(self, name=None, coach=None, formation=None):
        self.name=name
        self.coach=coach
        self.formation=formation
        

    def convertRawToClub(self,rawClub):
        self.name=rawClub.name.decode("utf-8")
        self.coach=rawClub.coach.decode("utf-8")
        

    def print(self):
        print(self.name)
        print(self.coach)