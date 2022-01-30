import shutil
import os
import json

def backup(folder, file, file_backup):
    if os.path.exists(file):
        os.makedirs(os.path.dirname(folder + '/'), exist_ok=True)
        shutil.copy(file, './' + folder + '/' + file_backup)
        print(file, 'duplication done')

def delete(file):
    if os.path.exists(file):
        os.remove(file)
    print(file, 'elimination done')

def saveJSON(JSONlist, file):
    with open(file, 'w') as json_file:
        json.dump(JSONlist, json_file, indent=4, separators=(',',': '))
        print('Json data saved')