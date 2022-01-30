import tweet_manager
import file_manager
import config

def main():

    print('\n\nTwitterPy\n\n')

    # Print config
    printConfig()


    # Old data duplication
    print("-------------------")
    file_manager.backup(config.backup_folder, config.export_csv + '.csv', config.export_csv_backup + '.csv')
    file_manager.backup(config.backup_folder, config.export_json + '.json', config.export_json_backup + '.json')
    file_manager.delete(config.export_csv)
    file_manager.delete(config.export_json)
    print("-------------------")
    print('\n')
    
    # Core & csv saving
    JSONlist = tweet_manager.fetch(config.min_likes, config.bearer_token, config.max_tweets, config.max_added_or_fetched, config.query, config.export_csv + '.csv', config.days_span)
    
    # Json saving
    file_manager.saveJSON(JSONlist, config.export_json + '.json')
    print('\n')

def printConfig():
    print('---- Settings ----')
    print('Bearer token: ', config.bearer_token)
    print('Max tweets ', config.max_tweets)
    print('Added/Fetched mode: ', config.max_added_or_fetched)
    print('Query: ', config.query)
    print('Days span: ', config.days_span)
    print('CSV export file name: ', config.export_csv)
    print('JSON export file name: ', config.export_json)
    print('Backup Folder: ', config.backup_folder)
    print('CSV backup file name: ', config.export_csv_backup)
    print('JSON backup file name: ', config.export_json_backup)
    print("-------------------")
    print('\n')

if __name__ == "__main__":
    main()