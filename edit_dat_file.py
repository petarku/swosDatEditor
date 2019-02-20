import struct
import json
import raw_file_class as rawFile
import swos_model as model

def trash():
    with open('partizan.json', 'r') as f:
        data = json.load(f)
        print(data['name'])
        print(data['coach'])

        for player in data['players']:
            print(player['name'])
            print(player['number'])
            print(player['desiredSum'])

def read_json_file(jsonFile):
    with open(jsonFile, 'r') as f:
        data = json.load(f)
        return data

def editDatFile(filename, data):

    
           

    fout = open(filename + '.new', 'wb')

    with open(filename, "r+b") as f:

            s = f.read(2)
            fout.write(s)
            numberOfTeamsInFile = int.from_bytes(s,byteorder='big')
            #print (numberOfTeamsInFile)
            var = 1
            s=f.read(76)
            
            while ( s!= b""):
                test,test1,test2,test3,clubNameRaw,rubbish,tacticNumber,league,shirtType,shirtColor,rubbish3,coachName ,rest = struct.unpack("BBHB16s3sBBBB8s22s18s", s)
                clubName = clubNameRaw.decode("utf-8")
                #clubName = clubName.strip()
                #print(coachName)
                #tactic = int.from_bytes(tacticNumber,byteorder='big')
                clubName= clubName[0:8]
                print(len(clubName))
                print(len(data['name']))
                if (clubName == data['name'] ) :
                    print("if prosao") 
                    clubNameEditByte = clubName.encode('utf-8')
                    coachNameEditByte = data['coach'].encode('utf-8')
                    fout.write(struct.pack("BBHB16s3sBBBB8s22s18s", test,test1,test2,test3,clubNameEditByte,rubbish,tacticNumber,league,shirtType,shirtColor,rubbish3,coachNameEditByte ,rest ))
                else: 
                    print("if ne prosao") 
                    fout.write(struct.pack("BBHB16s3sBBBB8s22s18s", test,test1,test2,test3,clubNameRaw,rubbish,tacticNumber,league,shirtType,shirtColor,rubbish3,coachName ,rest ))
                for x in range(0, 16):
                    s=f.read(38)

                    nationIndex,rubbish2,shirtNumber,playerNameRaw,rest2 = struct.unpack("BBB22s13s", s)
                    fout.write(struct.pack("BBB22s13s",nationIndex,rubbish2,shirtNumber,playerNameRaw,rest2))
                    playerName = playerNameRaw.decode(encoding="utf-8")
                        
                    print(playerName)
                        #print ('player Number {} '.format(x+1))
                        #print(playerName)
                
                s=f.read(76)
    fout.close     

def readDatFile(filename):
    

    with open(filename, "r+b") as f:

            numberOfTeamsRaw = f.read(2)
            raw = rawFile.RawDatFile()
            numberOfTeamsInFile = int.from_bytes(numberOfTeamsRaw,byteorder='big')
            raw.numberOfTeams = numberOfTeamsRaw 
            clubData = rawFile.RawClubData()
            s=f.read(76)
            
            while ( s != b""):
                countryNumber,teamOrdinal,globalTeamNumber,teamStatus,clubNameRaw,unused3,tacticNumber,league,shirtType,shirtColor,shirtSecondColor,shortsColor,socksColor,shirt2Type,shirt2Color,shirt2SecondColor,shorts2Color,socks2Color,coachName,unused2,playerIndices = struct.unpack("BBHB16s3sBBBBBBBBBBBB22s2s16s", s)
            
                clubData.tuple = countryNumber,teamOrdinal,globalTeamNumber,teamStatus,clubNameRaw,unused3,tacticNumber,league,shirtType,shirtColor,shirtSecondColor,shortsColor,socksColor,shirt2Type,shirt2Color,shirt2SecondColor,shorts2Color,socks2Color,coachName,unused2,playerIndices
                clubData.countryNumber = countryNumber
                clubData.name = clubNameRaw 
                clubData.coach = coachName
                clubData.teamOrdinal = teamOrdinal
                clubData.globalTeamNumber = globalTeamNumber
                clubData.teamStatus = teamStatus
                clubData.unused3 = unused3
                clubData.tacticNumber = tacticNumber 
                clubData.league = league 
                clubData.shirtType = shirtType
                clubData.shirtColor = shirtColor
                clubData.shirtSecondColor = shirtSecondColor 
                clubData.shortsColor = shortsColor 
                clubData.socksColor = socksColor 
                clubData.shirt2Type = shirt2Type
                clubData.shirt2Color = shirt2Color
                clubData.shirt2SecondColor = shirt2SecondColor 
                clubData.shorts2Color = shorts2Color 
                clubData.socks2Color = socks2Color 
                clubData.unused2 = unused2 
                clubData.playerIndices = playerIndices 
                
                for x in range(0, 16):
                    s=f.read(38)
                    playerData = rawFile.RawPlayerData()
                    nationIndex,unused1,shirtNumber,playerNameRaw,emptyByte,playerPosition,playerCards,unknownP,VH,TC,SF, playerPrice , rest2 = struct.unpack("BBB22sBBBBBBBB5s", s)
                    print(TC)
                    #print (hex(TC)) 
                    T, C = TC >> 4, TC & 0x0F
                    print(T, C)
                    #print (0x0F & hex(TC) )
                    playerName = playerNameRaw.decode(encoding="utf-8")
                    playerData.tuple = nationIndex,unused1,shirtNumber,playerNameRaw,emptyByte,playerPosition,playerCards,unknownP,VH,TC,SF, playerPrice , rest2 
                    playerData.nationIndex = nationIndex 

                    playerData.playerName = playerNameRaw
                    print(playerNameRaw)
                    playerData.unused1 = unused1 
                    playerData.playerShirtNo = shirtNumber 
                    #print(playerName)
                    clubData.add_players(playerData)
                    #print ('player Number {} '.format(x+1))
                    #print(playerName)
                rawFile.RawDatFile().add_club_data(clubData)
                s=f.read(76)
    return raw 



def writeDatFile(filename, RawDatFile):
    fout = open(filename + '.new', 'wb')
    fout.write(RawDatFile.numberOfTeams)
    numberOfTeamsInFile = int.from_bytes(RawDatFile.numberOfTeams,byteorder='big')
    print(numberOfTeamsInFile)
    
    for n in range(0,numberOfTeamsInFile):
        fout.write(struct.pack("BBHB16s3sBBBBBBBBBBBB22s2s16s", RawDatFile.rawClubData[n].tuple ))
        for i in range(0,16):
            fout.write(struct.pack("BBB22sBBBBBBBB5s",RawDatFile.rawClubData[n].rawPlayerData[i].tuple))
        
    fout.close


#data = read_json_file("partizan.json")   
#editDatFile("TEAM.070" , data)
fileRaw1 = readDatFile("TEAM.070")
club = model.Club()
club.convertRawToClub(fileRaw1.rawClubData[0])
club.print()
'''print(fileRaw1.numberOfTeams)
print(fileRaw1.rawClubData[0].name)
print(fileRaw1.rawClubData[0].tuple)
print(fileRaw1.rawClubData[0].rawPlayerData[0].playerShirtNo)
#print(fileRaw1.rawClubData[0].rawPlayerData[0].tuple) '''

#writeDatFile("TEAM.008", fileRaw1)