from csv import DictReader

with open('file_csv.csv', 'r') as f :
    csv_reader = DictReader(f)   # if using | or * instead of , then csv_reader = DictReader(f, delimiter = '|')
    # iterator so you can run loop on it
    for row in csv_reader :
        print(f"name is {row['name']} and email is {row['email']}")