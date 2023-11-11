import pickle
from tweet import Tweet

# Function to save tweets to a file
def save_tweets(tweets):
    with open("twitter.dat", "wb") as file:
        pickle.dump(tweets, file)

# Function to load tweets from a file
def load_tweets():
    try:
        with open("twitter.dat", "rb") as file:
            tweets = pickle.load(file)
        return tweets
    except FileNotFoundError:
        return []

# Function to make a new tweet
def make_tweet(tweets):
    author = input("\nWhat is your name? ")
    text = input("What would you like to tweet? ")
    
    while len(text) > 140:
        print("Tweet is too long. Please limit your tweet to 140 characters.")
        text = input("Enter your tweet: ")

    new_tweet = Tweet(author, text)
    tweets.append(new_tweet)
    save_tweets(tweets)  # Save tweets after adding a new tweet
    print("Your tweet has been saved.")

# Function to view recent tweets
def view_recent_tweets(tweets):
    if not tweets:
        print("No tweets available.")
    else:
        print("\nRecent Tweets:")
        print("------------------------")
        for tweet in tweets[-5:][::-1]:
            tweet.display_tweet()
            print("\n")

# Function to search through tweets
def search_tweets(tweets):
    if not tweets:
        print("No tweets available.")
    else:
        search_text = input("What would you like to search for? ")
        matching_tweets = [tweet for tweet in tweets if search_text.lower() in tweet.get_text().lower()]
        
        if not matching_tweets:
            print("No tweets found with the specified search text.")
        else:
            print("\nSearch Results")
            print("------------------------")
            for tweet in matching_tweets:
                tweet.display_tweet()
                print("\n")
                

# Main function
def main():
    tweets = load_tweets()

    while True:
        print("\nTweet Menu")
        print("-----------")
        print("1. Make a Tweet")
        print("2. View Recent Tweets")
        print("3. Search Tweets")
        print("4. Quit")

        choice = input("What would you like to do? ")

        if choice == "1":
            make_tweet(tweets)
        elif choice == "2":
            view_recent_tweets(tweets)
        elif choice == "3":
            search_tweets(tweets)
        elif choice == "4":
            save_tweets(tweets)  # Save tweets before exiting
            print("Thank you for using the Tweet Manager!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
