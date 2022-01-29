import requests
import os
import json
import csv
import datetime
import dateutil.parser
import unicodedata
import time
import config


def auth():
    return config.bearer_token

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/recent" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'max_results': max_results,
                    'expansions': 'author_id',
                    'tweet.fields': 'id,text,author_id,created_at,public_metrics',
                    'user.fields': 'id,name,username,public_metrics',
                    'next_token': {}}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def append_to_csv(json_response, fileName, result_count):

    #A counter variable
    counter = 0

    #Open OR create the target CSV file
    csvFile = open(fileName, "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_NONNUMERIC)

    #Loop through each tweet
    for tweet in json_response['data']:
        like_count = int(tweet['public_metrics']['like_count'])
        
        if(like_count > 0):
            author_id = tweet['author_id']
            
            created_at = dateutil.parser.parse(tweet['created_at'])
            
            tweet_id = tweet['id']
            
            text = tweet['text']
            
            followers_count = 0
            
            name = ""
            
            username = ""

            for user in json_response['includes']['users']:
                if user['id'] == author_id:
                    followers_count = int(user['public_metrics']['followers_count'])
                    name = user['name']
                    username = user['username']
            
            ratio = float(like_count / followers_count if followers_count else like_count)
            
            res = [ratio, text, created_at, username, name, tweet_id, like_count, followers_count, author_id]
            
            # Append the result to the CSV file
            csvWriter.writerow(res)
            counter += 1

    # When done, close the CSV file
    csvFile.close()

    # Print the number of tweets for this iteration
    print("# of Tweets added / fetched : ", counter, "/", result_count)
    return counter 


def main():
    #Inputs for tweets

    max_tweets = config.max_tweets
    max_fetched_added = config.max_added_or_fetched
    bearer_token = auth()
    headers = create_headers(bearer_token)
    keyword = config.query
    today = datetime.datetime.utcnow().date()
    yesterday = today - datetime.timedelta(days=1)
    max_results = 100

    #Total number of tweets we collected from the loop
    total_tweets = 0
    total_tweets_added = 0

    # Create file
    csvFile = open("data.csv", "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    #Create headers for the data you want to save, in this example, we only want save these columns in our dataset
    csvWriter.writerow(['ratio', 'text', 'created_at', 'username', 'name', 'tweet_id', 'like_count', 'followers_count', 'author_id'])
    csvFile.close()

    # Inputs
    count = 0 # Counting tweets per time period
    max_count = 100 # Max tweets per time period
    flag = True
    next_token = None
    
    # Check if flag is true
    while flag:
        # Check if max_count reached
        if max_fetched_added == 'fetched':
            if total_tweets >= max_tweets:      
                break
        else: 
            if max_fetched_added == 'added':
                if total_tweets_added >= max_tweets:      
                    break

        print("-------------------")
        print("Token: ", next_token)
        url = create_url(keyword, str(yesterday),str(today), max_results)
        json_response = connect_to_endpoint(url[0], headers, url[1], next_token)
        result_count = json_response['meta']['result_count']

        if 'next_token' in json_response['meta']:
            # Save the token to use for next call
            next_token = json_response['meta']['next_token']
            print("Next Token: ", next_token)
            if result_count is not None and result_count > 0 and next_token is not None:
                print("Start Date: ", str(yesterday))
                tmp_count = append_to_csv(json_response, "data.csv", result_count)
                count += result_count
                total_tweets_added += tmp_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("Total # of Tweets added: ", total_tweets_added)
                print("-------------------")
                time.sleep(5)                
        # If no next token exists
        else:
            if result_count is not None and result_count > 0:
                print("-------------------")
                print("Start Date: ", str(yesterday))
                tmp_count = append_to_csv(json_response, "data.csv", result_count)
                count += result_count
                total_tweets_added += tmp_count
                total_tweets += result_count
                print("Total # of Tweets fetched: ", total_tweets)
                print("Total # of Tweets added: ", total_tweets_added)
                print("-------------------")
                time.sleep(5)
            
            #Since this is the final request, turn flag to false to move to the next time period.
            flag = False
            next_token = None
        time.sleep(5)
    print("Total number of results: ", total_tweets)



if __name__ == "__main__":
    main()