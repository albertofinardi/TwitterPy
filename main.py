import tweet_manager
import file_manager
import config

def main():
    # Old data duplication
    file_manager.backup(config.backup_folder, config.export_csv, config.export_csv_backup)
    file_manager.backup(config.backup_folder, config.export_json, config.export_json_backup)
    file_manager.delete(config.export_csv)
    file_manager.delete(config.export_json)
    
    # Core & csv saving
    JSONlist = tweet_manager.fetch(config.bearer_token, config.max_tweets, config.max_added_or_fetched, config.query, config.export_csv)
    
    # Json saving
    file_manager.saveJSON(JSONlist, config.export_json)

if __name__ == "__main__":
    main()