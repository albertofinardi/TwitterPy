import tweet_manager
import file_manager
import config

def main():

    print('\n\nTwitterPy\n\n')
    # Old data duplication
    file_manager.backup(config.backup_folder, config.export_csv + '.csv', config.export_csv_backup + '.csv')
    file_manager.backup(config.backup_folder, config.export_json + '.json', config.export_json_backup + '.json')
    file_manager.delete(config.export_csv)
    file_manager.delete(config.export_json)
    print('\n')
    
    # Core & csv saving
    JSONlist = tweet_manager.fetch(config.bearer_token, config.max_tweets, config.max_added_or_fetched, config.query, config.export_csv + '.csv', config.days_span)
    
    # Json saving
    file_manager.saveJSON(JSONlist, config.export_json + '.json')
    print('\n')

if __name__ == "__main__":
    main()