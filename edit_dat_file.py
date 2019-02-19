import struct
import json
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

            s = f.read(2)
            
            numberOfTeamsInFile = int.from_bytes(s,byteorder='big')
            var = 1
            s=f.read(76)
            
            while ( s != b""):
                test,test1,test2,test3,clubNameRaw,rubbish,tacticNumber,league,shirtType,shirtColor,rest = struct.unpack("BBHB16s3sBBBB48s", s)
                clubName = clubNameRaw.decode(encoding="utf-8")
                #tactic = int.from_bytes(tacticNumber,byteorder='big')
                print(clubName)
                clubName = "Partizan"
                print(clubName)
                print(league)
                b = clubName.encode('utf-8')
                print(b)
                
                #print(shirtType)
                #print(shirtColor)
                for x in range(0, 16):
                    s=f.read(38)

                    nationIndex,rubbish2,shirtNumber,playerNameRaw,rest2 = struct.unpack("BBB22s13s", s)
                    
                    playerName = playerNameRaw.decode(encoding="utf-8")
                    
                    print(playerName)
                    #print ('player Number {} '.format(x+1))
                    #print(playerName)
                s=f.read(76)
              


data = read_json_file("partizan.json")   
editDatFile("TEAM.070" , data)
#readDatFile("TEAM.070")