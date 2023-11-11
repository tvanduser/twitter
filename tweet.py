import datetime

class Tweet:
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = datetime.datetime.now()

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        current_time = datetime.datetime.now()
        age_delta = current_time - self.__age

        # Calculate seconds, minutes, and hours
        seconds = age_delta.seconds
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        # Format the time difference as a string
        if hours > 0:
            return f"{hours}h"
        elif minutes > 0:
            return f"{minutes}m"
        else:
            return f"{seconds}s"

    def display_tweet(self):
        print(f"{self.__author} - {self.get_age()}")
        print(f"{self.__text}")
        #print(f"Age: f"{self.get_age()}")
