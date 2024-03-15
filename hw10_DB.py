import datetime
import os
import xml.etree.ElementTree as ET
import sqlite3

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

class XMLReader:
    def __init__(self, filename):
        self.filename = filename

    def read_records(self):
        records = []
        tree = ET.parse(self.filename)
        root = tree.getroot()
        for record in root:
            record_data = {}
            for item in record:
                record_data[item.tag] = item.text
            records.append(record_data)
        return records

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_connection(self):
        return sqlite3.connect(self.db_file)

    def check_duplicate(self, table, data):
        conn = self.create_connection()
        cur = conn.cursor()
        query = f"SELECT * FROM {table} WHERE "
        conditions = []
        for key, value in data.items():
            conditions.append(f"{key} = '{value}'")
        query += " AND ".join(conditions)
        cur.execute(query)
        duplicate = cur.fetchone() is not None
        conn.close()
        return duplicate

    def insert_record(self, table, data):
        conn = self.create_connection()
        cur = conn.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        values = tuple(data.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cur.execute(query, values)
        conn.commit()
        conn.close()

def main():
    news_feed = NewsFeed('output.txt')  # Specify the output file for NewsFeed
    file_processor = FileProcessor('.')  # Default folder for file processing
    db_manager = DatabaseManager('news_database.db')  # Database manager

    while True:
        print("1. Add news")
        print("2. Add private ad")
        print("3. Add custom record")
        print("4. Process file")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice in {'1', '2', '3'}:
            xml_file = input("Enter the XML file path: ")
            if os.path.exists(xml_file):
                xml_reader = XMLReader(xml_file)
                records = xml_reader.read_records()
                if choice == '1':
                    for record in records:
                        if not db_manager.check_duplicate('news', record):
                            db_manager.insert_record('news', record)
                            news_feed.add_news(record.get('text', ''), record.get('city', ''))
                            print("News added successfully.")
                        else:
                            print("Duplicate record found. Skipping...")
                elif choice == '2':
                    for record in records:
                        if not db_manager.check_duplicate('private_ads', record):
                            db_manager.insert_record('private_ads', record)
                            news_feed.add_private_ad(record.get('text', ''), record.get('expiration_date', ''))
                            print("Private ads added successfully.")
                        else:
                            print("Duplicate record found. Skipping...")
                elif choice == '3':
                    for record in records:
                        if not db_manager.check_duplicate('custom_records', record):
                            db_manager.insert_record('custom_records', record)
                            news_feed.add_custom(record.get('text', ''))
                            print("Custom records added successfully.")
                        else:
                            print("Duplicate record found. Skipping...")
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
