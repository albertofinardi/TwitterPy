import tweet_manager
import file_manager

def start(bearer_token, max_tweets, min_likes, max_added_or_fetched, query, days_span, export_csv, export_json, backup_folder, export_csv_backup, export_json_backup):

    print('\n\nTwitterPy\n\n')

    # Print config
    printConfig(bearer_token, max_tweets, min_likes, max_added_or_fetched, query, days_span, export_csv, export_json, backup_folder, export_csv_backup, export_json_backup)


    # Old data duplication
    print("-------------------")
    file_manager.backup(backup_folder, export_csv + '.csv', export_csv_backup + '.csv')
    file_manager.backup(backup_folder, export_json + '.json', export_json_backup + '.json')
    file_manager.delete(export_csv + '.csv')
    file_manager.delete(export_json + '.json')
    print("-------------------")
    print('\n')
    
    # Core & csv saving
    JSONlist = tweet_manager.fetch(int(min_likes), bearer_token, int(max_tweets), max_added_or_fetched, query, export_csv + '.csv', int(days_span))
    
    # Json saving
    file_manager.saveJSON(JSONlist, export_json + '.json')
    print('\n')

def printConfig(bearer_token, max_tweets, min_likes, max_added_or_fetched, query, days_span, export_csv, export_json, backup_folder, export_csv_backup, export_json_backup):
    print('---- Settings ----')
    print('Bearer token: ', bearer_token)
    print('Max tweets ', max_tweets)
    print('Min likes ', min_likes)
    print('Added/Fetched mode: ', max_added_or_fetched)
    print('Query: ', query)
    print('Days span: ', days_span)
    print('CSV export file name: ', export_csv)
    print('JSON export file name: ', export_json)
    print('Backup Folder: ', backup_folder)
    print('CSV backup file name: ', export_csv_backup)
    print('JSON backup file name: ', export_json_backup)
    print("-------------------")
    print('\n')