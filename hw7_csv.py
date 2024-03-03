import datetime
import os
import collections
import csv

class NewsFeed:
    def __init__(self, filename):
        self.filename = filename

    def add_news(self, text, city):
        date = datetime.date.today()
        with open(self.filename, 'a') as file:
            file.write(f"News:\nText: {text}\nCity: {city}\nDate: {date}\n\n")
        self.update_counts(text)

    def add_private_ad(self, text, expiration_date):
        date_today = datetime.date.today()
        expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        days_left = (expiration_date - date_today).days
        with open(self.filename, 'a') as file:
            file.write(f"Private Ad:\nText: {text}\nDays left: {days_left}\n\n")
        self.update_counts(text)

    def add_custom(self, text):
        with open(self.filename, 'a') as file:
            file.write(f"Custom:\nText: {text}\n\n")
        self.update_counts(text)

    def update_counts(self, text):
        words = text.lower().split()
        letters = [ch for ch in text if ch.isalpha()]
        uppercase = [ch for ch in text if ch.isupper()]

        word_counts = collections.Counter(words)
        letter_counts = collections.Counter(letters)

        with open('word_count.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Word', 'Count'])
            for word, count in word_counts.items():
                writer.writerow([word, count])

        with open('letter_count.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Letter', 'Count_All', 'Count_Uppercase', 'Percentage'])
            for letter, count in letter_counts.items():
                uppercase_count = uppercase.count(letter)
                percentage = (uppercase_count / count) * 100
                writer.writerow([letter, count, uppercase_count, percentage])

class FileProcessor:
    def __init__(self, folder):
        self.folder = folder

    def process_file(self, filename):
        filepath = os.path.join(self.folder, filename)
        # Process the file
        print(f"Processing file: {filepath}")
        # Remove the file if it was successfully processed
        os.remove(filepath)
        print(f"File {filename} removed.")

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_records(self):
        with open(self.filename, 'r') as file:
            records = file.readlines()
        return records

def main():
    news_feed = NewsFeed('output.txt')  # Specify the output file for NewsFeed
    file_processor = FileProcessor('.')  # Default folder for file processing

    while True:
        print("1. Add news")
        print("2. Add private ad")
        print("3. Add custom record")
        print("4. Process file")
        print("5. Quit")
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
            filename = input("Enter the filename to process: ")
            file_processor.process_file(filename)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
