from csv import reader

with open('file_csv.csv', 'r') as f :
    csv_reader = reader(f)
    # iterator so you can run loop on it
    next(csv_reader)
    for row in csv_reader :
        print(row)