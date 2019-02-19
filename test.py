from edit_dat_file import editDatFile
import json
with open('partizan.json', 'r') as f:
    array = json.load(f)

def test_file_open():
    editDatFile("TEAM.070" , "partizan.json") 
    