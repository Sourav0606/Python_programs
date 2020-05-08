# writer, DictWriter

from csv import writer

with open('file2_csv.csv', 'w', newline = '') as f :
    csv_writer = writer(f)
    # methods - writerow, writerows
    # csv_writer.writerow(['name', 'country'])
    # csv_writer.writerow(['sourav', 'india'])
    # csv_writer.writerow(['guddu', 'india'])

    csv_writer.writerows([['name', 'country'], ['sourav', 'india'], ['guddu', 'india']])