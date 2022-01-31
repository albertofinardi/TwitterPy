import json
import file_manager
import os

configFile = 'config.json'

def config():
    if os.path.exists(configFile):
        with open(configFile, 'r') as f:
            config = json.load(f)
            bearer_token = config['bearer_token']
            max_tweets = int(config['max_tweets'])
            min_likes = int(config['max_tweets'])
            max_added_or_fetched = config['max_added_or_fetched']
            query = config['query']
            days_span = int(config['days_span'])
            export_csv = config['export_csv']
            export_json = config['export_json']
            backup_folder = config['backup_folder']
            export_csv_backup = config['export_csv_backup']
            export_json_backup = config['export_json_backup']
            return bearer_token, max_tweets, min_likes, max_added_or_fetched, query, days_span, export_csv, export_json, backup_folder, export_csv_backup, export_json_backup
    else:
        initialization()
        with open(configFile, 'r') as f:
            config = json.load(f)
            bearer_token = config['bearer_token']
            max_tweets = int(config['max_tweets'])
            min_likes = int(config['max_tweets'])
            max_added_or_fetched = config['max_added_or_fetched']
            query = config['query']
            days_span = int(config['days_span'])
            export_csv = config['export_csv']
            export_json = config['export_json']
            backup_folder = config['backup_folder']
            export_csv_backup = config['export_csv_backup']
            export_json_backup = config['export_json_backup']
            return bearer_token, max_tweets, min_likes, max_added_or_fetched, query, days_span, export_csv, export_json, backup_folder, export_csv_backup, export_json_backup


def save(bearer_token, max_tweets, min_likes, max_added_or_fetched, query, days_span, export_csv, export_json, backup_folder, export_csv_backup, export_json_backup):
    config = {
        "bearer_token": str(bearer_token),
        "max_tweets" : int(max_tweets),
        "min_likes" : int(min_likes),
        "max_added_or_fetched" : str(max_added_or_fetched),
        "query" : str(query),
        "days_span" : int(days_span),
        "export_csv" : str(export_csv),
        "export_json" : str(export_json),
        "backup_folder" : str(backup_folder),
        "export_csv_backup" : str(export_csv_backup),
        "export_json_backup" : str(export_json_backup)
    }
    file_manager.saveJSON(config, configFile)

def initialization():
    file_manager.configInitialization(configFile)