import struct

filename = "TEAM.070"
fout = open(filename + '.new', 'wb')

with open(filename, "r+b") as f:

    s = f.read(2)
    fout.write(s)
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
        fout.write(struct.pack("BBHB16s3sBBBB48s", test,test1,test2,test3,b,rubbish,tacticNumber,league,shirtType,shirtColor,rest))
        #print(shirtType)
        #print(shirtColor)
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