# TwitterPy

## Getting started

Download the code and run ```python3 main.py``` in your console (python3 needed). If python not installed, see [here](https://phoenixnap.com/kb/how-to-install-python-3-windows).

GUI application params:
| Variable | Deafult | Type | Meaning |
| ------ | ------ | ------ | ------ |
| ```bearer_token``` | -- | String | Bearer token of your twitter developer account. See [here](https://developer.twitter.com/en/docs/platform-overview). |
| ```max_tweets``` | 500 | Int | Max number of results. |
| ```min_likes``` | 0 | Int | Min number of likes per tweet. |
| ```max_added_or_fetched``` | ```fetched``` | ```fetched``` or ```added``` (String) | If ```fetched```, ```max_tweets``` indicates the maximum number of tweets downloaded from twitter. If ```added```, ```max_tweets``` indicates the maximum number of tweets with at least 1 like. If empty, there's no limit. |
| ```query``` | "$tsla" lang:en -is:verified -has:hashtags -has:links -has:videos -is:retweet -is:reply -has:mentions | String | Query filters. See [here](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule). |
| ```days_span``` | 1 | Int | Says from today for data acquisition (1 = from yesterday to today). |
| ```export_csv``` | data | String | Name of csv export file (without extension). |
| ```export_json``` | data | String | Name of json export file (without extension). |
| ```backup_folder``` | backup | String | Name of the folder for backup data (without extension). |
| ```export_csv_backup``` | data_backup | String | Name of csv backup file (without extension). |
| ```export_json_backup``` | data_backup | String | Name of json backup file (without extension). |

To see the program status, look at the terminal output.