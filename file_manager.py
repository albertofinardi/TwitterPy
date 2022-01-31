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
    print(file, 'deleted')

def saveJSON(JSONlist, file):
    with open(file, 'w') as json_file:
        json.dump(JSONlist, json_file, indent=4, separators=(',',': '))
        print(file, 'saved')
    
def configInitialization(file):
    if not os.path.exists(file):
        config = {
            "bearer_token": "",
            "max_tweets" : 500,
            "min_likes" : 0,
            "max_added_or_fetched" : "fetched",
            "query" : '"$tsla" lang:en -is:verified -has:hashtags -has:links -has:videos -is:retweet -is:reply -has:mentions',
            "days_span" : 1,
            "export_csv" : "data",
            "export_json" : "data",
            "backup_folder" : "backup",
            "export_csv_backup" : "data_backup",
            "export_json_backup" : "data_backup"
        }
        saveJSON(config, file)
