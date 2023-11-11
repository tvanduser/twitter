
from tweet import Tweet  # Assuming the Tweet class is in a separate file named Tweet.py
#make a new tweet
def make_tweet(tweets):
    author = input("Enter your name: ")
    text = input("Enter your tweet (140 characters max): ")
    #make sure tweet is correct length 
    while len(text) > 140:
        print("Tweet is too long. Please limit your tweet to 140 characters.")
        text = input("Enter your tweet (140 characters max): ")
    #post the tweet by adding it to the tweets array 
    new_tweet = Tweet(author, text)
    tweets.append(new_tweet)
    print("Tweet successfully posted!")
#view the recent tweets 
def view_recent_tweets(tweets):
    if not tweets:
        print("No tweets available.")
    else:
        print("\nRecent Tweets:")
        print("------------------------")
        for tweet in tweets[-5:][::-1]:  # Display the five most recent tweets in reverse order
            tweet.display_tweet()
            print("\n")
            
#search through the tweets 
def search_tweets(tweets):
    if not tweets:
        print("No tweets available.")
    else:
        search_text = input("Enter the text to search for in tweets: ")
        #convert everything to lowercase and then searching for matches withing the tweets array 
        matching_tweets = [tweet for tweet in tweets if search_text.lower() in tweet.get_text().lower()]
        #nothing matches: this is what happens 
        if not matching_tweets:
            print("No tweets found with the specified search text.")
        else:
            print("Matching Tweets:")
            for tweet in matching_tweets:
                tweet.display_tweet()
                print("------------------------")

def main():
    tweets = []

    while True:
        #display the menu 
        print("\nTweet Menu")
        print("-----------")
        print("1. Make a Tweet")
        print("2. View Recent Tweets")
        print("3. Search Tweets")
        print("4. Quit")
        #get what the user wants to do 
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            make_tweet(tweets)
        elif choice == "2":
            view_recent_tweets(tweets)
        elif choice == "3":
            search_tweets(tweets)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
#run the programm by getting it to go into main 
if __name__ == "__main__":
    main()
