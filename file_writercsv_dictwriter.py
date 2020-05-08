from csv import DictWriter

with open('file3_csv.csv', 'w', newline = '') as f :
    csv_writer = DictWriter(f, fieldnames = ['first_name', 'last_name', 'age'])
    csv_writer.writeheader()
    # methods - writerow, writerows
    csv_writer.writerow({
        'first_name' : 'sourav',
        'last_name' : 'rai',
        'age' : 21
    })
    
    csv_writer.writerow({
        'first_name' : 'guddu',
        'last_name' : 'rai',
        'age' : 22
    })

    csv_writer.writerows([
        {'first_name' : 'sourav',
        'last_name' : 'rai',
        'age' : 21},
        {'first_name' : 'guddu',
        'last_name' : 'rai',
        'age' : 22}
    ])