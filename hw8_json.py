import datetime
import os
import json

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

class JSONReader:
    def __init__(self, filename):
        self.filename = filename

    def read_records(self):
        with open(self.filename, 'r') as file:
            records = json.load(file)
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
            json_file = input("Enter the JSON file path for news: ")
            if os.path.exists(json_file):
                json_reader = JSONReader(json_file)
                records = json_reader.read_records()
                for record in records:
                    news_feed.add_news(record['text'], record['city'])
                print("News added successfully.")
            else:
                print("File not found.")
        elif choice == '2':
            json_file = input("Enter the JSON file path for private ads: ")
            if os.path.exists(json_file):
                json_reader = JSONReader(json_file)
                records = json_reader.read_records()
                for record in records:
                    news_feed.add_private_ad(record['text'], record['expiration_date'])
                print("Private ads added successfully.")
            else:
                print("File not found.")
        elif choice == '3':
            json_file = input("Enter the JSON file path for custom records: ")
            if os.path.exists(json_file):
                json_reader = JSONReader(json_file)
                records = json_reader.read_records()
                for record in records:
                    news_feed.add_custom(record['text'])
                print("Custom records added successfully.")
            else:
                print("File not found.")
        elif choice == '4':
            filename = input("Enter the filename to process: ")
            file_processor.process_file(filename)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
