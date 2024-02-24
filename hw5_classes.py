import datetime

class NewsFeed:
    def __init__(self, filename):
        self.filename = filename

    def add_news(self, text, city):
        date = datetime.date.today()
        with open(self.filename, 'a') as file:
            file.write(f"News:\nText: {text}\nCity: {city}\nDate: {date}\n\n")

    def add_private_ad(self, text, expiration_date):
        date_today = datetime.date.today()
        expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        days_left = (expiration_date - date_today).days
        with open(self.filename, 'a') as file:
            file.write(f"Private Ad:\nText: {text}\nDays left: {days_left}\n\n")

    def add_custom(self, text):
        with open(self.filename, 'a') as file:
            file.write(f"Custom:\nText: {text}\n\n")

def main():
    news_feed = NewsFeed('news_feed.txt')

    while True:
        print("1. Add news")
        print("2. Add private ad")
        print("3. Add custom record")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter the news text: ")
            city = input("Enter the city: ")
            news_feed.add_news(text, city)
        elif choice == '2':
            text = input("Enter the ad text: ")
            expiration_date = input("Enter the expiration date (YYYY-MM-DD): ")
            news_feed.add_private_ad(text, expiration_date)
        elif choice == '3':
            text = input("Enter the custom record text: ")
            news_feed.add_custom(text)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()